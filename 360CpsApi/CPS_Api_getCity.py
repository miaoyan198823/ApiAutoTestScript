# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getCity_Sign
import urllib



class GetCiytApi():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCity'
        params = getCity_Sign.new_sign()
        headers = getCity_Sign.get_headers()


    def test_getCity_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data']['city_id'] == '2419'
                assert dict_result_data['data']['city_name'] == u'北京'
                assert dict_result_data['data']['pid'] == '21'
                assert dict_result_data['data']['pname'] == u'北京'
        except requests.HTTPError,e:
            print e.message









