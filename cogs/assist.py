from discord.ext import commands
import discord
import os
import asyncio
import json
import click
import functools
from arsenic import get_session
from arsenic import browsers
from arsenic import services
import google.auth.transport.grpc
import google.auth.transport.requests
import google.oauth2.credentials
from google.assistant.embedded.v1alpha2 import (
	embedded_assistant_pb2,
	embedded_assistant_pb2_grpc
)
from asyncio.subprocess import DEVNULL

import assistant_helpers
import browser_helpers
import audio_helpers

ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com'
DEFAULT_GRPC_DEADLINE = 60 * 3 + 5
PLAYING = embedded_assistant_pb2.ScreenOutConfig.PLAYING

class GoogleAssistant(object):
	def __init__(self, language_code, device_model_id, device_id,
				 display, channel, deadline_sec):
		self.language_code = language_code
		self.device_model_id = device_model_id
		self.device_id = device_id
		self.conversation_state = None
		self.is_new_conversation = True
		self.display = display
		self.assistant = embedded_assistant_pb2_grpc.EmbeddedAssistantStub(
			channel
		)
		self.deadline = deadline_sec

	def __enter__(self):
		return self

	def __exit__(self, etype, e, traceback):
		if e:
			return False

	def assist(self, text_query, conversation_stream):
		"""Send a text request to the Assistant and playback the response.
		"""
		def iter_assist_requests():
			config = embedded_assistant_pb2.AssistConfig(
				audio_out_config=embedded_assistant_pb2.AudioOutConfig(
					encoding='LINEAR16',
					sample_rate_hertz=16000,
					volume_percentage=0,
				),
				dialog_state_in=embedded_assistant_pb2.DialogStateIn(
					language_code=self.language_code,
					conversation_state=self.conversation_state,
					is_new_conversation=self.is_new_conversation,
				),
				device_config=embedded_assistant_pb2.DeviceConfig(
					device_id=self.device_id,
					device_model_id=self.device_model_id,
				),
				text_query=text_query,
			)
			# Continue current conversation with later requests.
			self.is_new_conversation = False
			if self.display:
				config.screen_out_config.screen_mode = PLAYING
			req = embedded_assistant_pb2.AssistRequest(config=config)
			assistant_helpers.log_assist_request_without_audio(req)
			yield req

		text_response = None
		html_response = None
		for resp in self.assistant.Assist(iter_assist_requests(),
										  self.deadline):
			assistant_helpers.log_assist_response_without_audio(resp)
			conversation_stream.write(resp.audio_out.audio_data)
			if resp.screen_out.data:
				html_response = resp.screen_out.data
			if resp.dialog_state_out.conversation_state:
				conversation_state = resp.dialog_state_out.conversation_state
				self.conversation_state = conversation_state
			if resp.dialog_state_out.supplemental_display_text:
				text_response = resp.dialog_state_out.supplemental_display_text
		return text_response, html_response

	def assist_text(self, text_query):
		"""Send a text request to the Assistant and receive text back.
		"""
		def iter_assist_requests():
			config = embedded_assistant_pb2.AssistConfig(
				audio_out_config=embedded_assistant_pb2.AudioOutConfig(
					encoding='LINEAR16',
					sample_rate_hertz=16000,
					volume_percentage=0,
				),
				dialog_state_in=embedded_assistant_pb2.DialogStateIn(
					language_code=self.language_code,
					conversation_state=self.conversation_state,
					is_new_conversation=self.is_new_conversation,
				),
				device_config=embedded_assistant_pb2.DeviceConfig(
					device_id=self.device_id,
					device_model_id=self.device_model_id,
				),
				text_query=text_query,
			)
			# Continue current conversation with later requests.
			self.is_new_conversation = False
			if self.display:
				config.screen_out_config.screen_mode = PLAYING
			req = embedded_assistant_pb2.AssistRequest(config=config)
			assistant_helpers.log_assist_request_without_audio(req)
			yield req

		text_response = 'Google Assistant gave no response'
		html_response = None
		for resp in self.assistant.Assist(iter_assist_requests(),
										  self.deadline):
			assistant_helpers.log_assist_response_without_audio(resp)
			if resp.screen_out.data:
				html_response = resp.screen_out.data
			if resp.dialog_state_out.conversation_state:
				conversation_state = resp.dialog_state_out.conversation_state
				self.conversation_state = conversation_state
			if resp.dialog_state_out.supplemental_display_text:
				text_response = resp.dialog_state_out.supplemental_display_text
		if any(p in text_response.lower() for p in ['public ip', 'ip address', '::; 1']):
			text_response = 'I need permission to display that information'
		return text_response, html_response

try:
	with open(os.path.join(click.get_app_dir('google-oauthlib-tool'), 'credentials.json'), 'r') as f:
		credentials = google.oauth2.credentials.Credentials(token=None,
															**json.load(f))
		http_request = google.auth.transport.requests.Request()
		credentials.refresh(http_request)
except Exception as e:
	print('Failed to connect to Google Assistant. ') # Before cog is loaded so no bot.logger :(
	credentials = None

grpc_channel = google.auth.transport.grpc.secure_authorized_channel(credentials, http_request, ASSISTANT_API_ENDPOINT)
gassistant = GoogleAssistant('en-us', 'fire0682-444871677176709141', '287698408855044097', True, grpc_channel, DEFAULT_GRPC_DEADLINE)

class Assistant(commands.Cog, name='Google Assistant'):
	def __init__(self, bot):
		self.bot = bot
		self.responses = {}
		self.google = gassistant
		self.service = services.Chromedriver(log_file=DEVNULL)
		self.browser = browsers.Chrome(chromeOptions={
			'args': ['--headless', '--disable-gpu', '--log-file=/dev/null']
		})

	def assist(self, user, query):
		text, html = self.google.assist_text(query)
		self.responses[user] = html or False

	@commands.command(description="Ask the Google Assistant a question.")
	@commands.max_concurrency(1, per=commands.BucketType.user)
	async def google(self, ctx, *, query):
		await ctx.channel.trigger_typing()
		try:
			await self.bot.loop.run_in_executor(None, func=functools.partial(self.assist, ctx.author.id, query))
		except Exception as e:
			if 'text_query too long.' in str(e):
				return await ctx.error(f'That query is too long. Try something shorter')
			return await ctx.error(f'Something went wrong.')
		if ctx.author.id not in self.responses:
			return await ctx.send(f'<a:okaygoogle:661951491082551306> Something went wrong. Try again later')
		async with get_session(self.service, self.browser) as session:
			await session.set_window_size(1920, 1080)
			sub = 'devapi' if self.bot.dev else 'api'
			await session.get(f'https://{sub}.gaminggeek.dev/assist/{ctx.author.id}')
			try:
				await session.execute_script('document.body.style.backgroundImage = \'url("https://picsum.photos/1920/1080")\';')
				namere = '<div class=\"show_text_content\">Your name is .*\.<\/div>'
				namesub = f'<div class=\'show_text_content\'>Your name is {ctx.author.name}.</div>'
				await session.execute_script(f'document.body.innerHTML = document.body.innerHTML.replace(/{namere}/gm, "{namesub}");')
				namere = '<div class=\"show_text_content\">I remember you telling me your name was .*\.<\/div>'
				namesub = f'<div class=\'show_text_content\'>I remember you telling me your name was {ctx.author.name}.</div>'
				await session.execute_script(f'document.body.innerHTML = document.body.innerHTML.replace(/{namere}/gm, "{namesub}");')
			except Exception:
				pass
				# await ctx.error('script did an oopsie')
			await asyncio.sleep(1.5)
			await ctx.send(file=discord.File((await session.get_screenshot()), filename='google.png'))
			return await session.close()
		return await ctx.error('If you\'re seeing this, something went wrong I guess ¯\_(ツ)_/¯')


def setup(bot):
	try:    
		bot.add_cog(Assistant(bot))
		print("Loaded assist.py")
	except Exception as e:
		print(f"Error loading assist.py: {e}")