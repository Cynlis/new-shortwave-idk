import requests

def version():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['version']
        return res


class Now:
    def artist():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['now']['artist']
        return res
    def song():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['now']['song']
        return res
    def encoderError():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['now']['encoderError']
        return res
class Listeners:
    def current():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['listeners']['current']
        return res
    def peak():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['listeners']['peak']
        return res

class Presenter:
    def username():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['presenter']['username']
        return res
    def autodj():
        url = "https://api.dual.pw/stats"
        r = requests.get(url)
        res = r.json()['presenter']['autoDJ']
        return res

