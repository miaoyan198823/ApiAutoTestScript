# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getCpsBill_Sign

class GetCpsBill(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCpsBill'
        self.params = getCpsBill_Sign.new_sign()
        self.headers = getCpsBill_Sign.get_headers()

class TestGetCpsBill(object):
    @pytest.fixture(scope='module')
    def gb(self):
        return GetCpsBill()

    def test_getCpsBill_api(self,gb):
        try:
            response = requests.get(gb.api_url,params=gb.params,headers=gb.headers,timeout=10)
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

