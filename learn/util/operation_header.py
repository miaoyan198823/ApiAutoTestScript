# -*- coding: utf-8 -*-
# @Time : 2019/9/9 16:34
# @Author : miaoyan


import requests
from util import operation_json



def get_token():
    url = operation_json.OperationJson().get_keywords("loginUrl")
    data = operation_json.OperationJson().get_keywords("loginData")
    try:
        res = requests.post(url, data).json()
        if 'access_token' and 'token_type' in res:
            auth_token = "{} {}".format(res['token_type'].capitalize(), res['access_token'])
            return auth_token
        else:
            return res
    except Exception as e:
        return ("error_info:".format(str(e)))

