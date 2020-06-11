import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self, jsonData, headers):
        return requests.post(url=self.login_url, json=jsonData, headers=headers)
