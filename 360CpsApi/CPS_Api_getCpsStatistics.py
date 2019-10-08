# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getCpsStatistics_Sign


class GetCpsStatistics():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCpsStatistics'
        params = getCpsStatistics_Sign.new_sign()
        headers = getCpsStatistics_Sign.get_headers()


    def test_getCpsStatistics_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data']['total_bill'] == '0.30'
                assert dict_result_data['data']['msg'] == u'已验证'
                assert dict_result_data['data']['status'] == '1'
        except requests.HTTPError,e:
            print e.message

