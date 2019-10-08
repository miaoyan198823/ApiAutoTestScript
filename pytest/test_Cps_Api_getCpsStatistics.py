# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getCpsStatistics_Sign


class GetCpsStatistics(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCpsStatistics'
        self.params = getCpsStatistics_Sign.new_sign()
        self.headers = getCpsStatistics_Sign.get_headers()

class TestGetCpsStatistics(object):
    @pytest.fixture(scope='module')
    def gs(self):
        return GetCpsStatistics()

    def test_getCpsStatistics_api(self,gs):
        try:
            response = requests.get(gs.api_url,params=gs.params,headers=gs.headers,timeout=10)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data']['total_bill'] == '0.30'
                assert dict_result_data['data']['msg'] == u'已验证'
                assert dict_result_data['data']['status'] == '1'
        except requests.HTTPError,e:
            print e.message

