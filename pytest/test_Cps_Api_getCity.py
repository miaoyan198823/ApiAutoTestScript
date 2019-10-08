# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getCity_Sign


class GC(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCity'
        self.params = getCity_Sign.new_sign()
        self.headers = getCity_Sign.get_headers()

class TestGetCity(object):
    @pytest.fixture(scope="module")
    def gc(self):
        return GC()

    def test_getCity_api(self,gc):
        try:
            response = requests.get(gc.api_url,params=gc.params,headers=gc.headers,timeout=10)
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









