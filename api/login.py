# -*- coding: utf-8 -*-

from api import readConfig as rc
import requests


def login(host,phone,password):
    url = "{}{}".format(rc.read_json()['url'][str(host)],rc.read_json()['path']['login'])
    data = {
        'phone':str(phone),
        'password':str(password)
    }
    res = requests.post(url=url,data=data)
    if 'access_token' and 'token_type' in res.text:
        auth_token = "{} {}".format(res.json()['token_type'].capitalize(),res.json()['access_token'])
        if auth_token:
            return auth_token
        else:
            return res.text
            # print("login_token:" + '\n' + auth_token)







