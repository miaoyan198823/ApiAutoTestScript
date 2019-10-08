# -*- coding: utf-8 -*-

from api import readConfig as rc
from api import login as l


def get_headers(host,phone,password):
    headers = rc.read_json()['headers']
    headers['Authorization'] = l.login(host,phone,password)
    headers['Host'] = "api-sandbox.hxgp.com"
    return headers


# print(get_headers('161','13511012200','123123123'))