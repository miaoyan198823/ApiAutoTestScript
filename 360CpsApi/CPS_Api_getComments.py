# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getComments_Sign



class GetCommentsApi():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getComments'
        params = getComments_Sign.new_sign()
        headers = getComments_Sign.get_headers()

    def test_getComments_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['user_name'] == u'm***92'
                assert dict_result_data['data'][0]['score'] == '5.0'
                assert dict_result_data['data'][0]['add_time'] == '2014-12-25 10:26:27'
                assert dict_result_data['data'][0]['content'] == u'真的不错.有机会还会去的'
        except requests.HTTPError,e:
            print e.message


