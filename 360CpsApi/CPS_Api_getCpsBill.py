# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getCpsBill_Sign


class GetCpsBill():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCpsBill'
        params = getCpsBill_Sign.new_sign()
        headers = getCpsBill_Sign.get_headers()

    def test_getCpsBill_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['id'] == '6'
                assert dict_result_data['data'][0]['fee'] == '3.00'
                assert dict_result_data['data'][0]['re_fee'] == '0.09'
                assert dict_result_data['data'][0]['status'] == '1'
                assert dict_result_data['data'][0]['cps_status'] == '1'
        except requests.HTTPError,e:
            print e.message

