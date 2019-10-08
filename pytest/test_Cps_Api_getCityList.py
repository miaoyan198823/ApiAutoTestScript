# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getCityList_Sign


class GL(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCityList'
        self.params = getCityList_Sign.new_sign()
        self.headers = getCityList_Sign.get_headers()

class TestGetCityList(object):
    @pytest.fixture(scope='module')
    def gl(self):
        return GL()
    def test_getCityList_api(self,gl):
        try:
            response = requests.get(gl.api_url,params=gl.params,headers=gl.headers,timeout=10)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['city_id'] == '4'
                assert dict_result_data['data'][-1]['city_id'] == '18'
                assert dict_result_data['data'][0]['city_name'] == u'淮北'
                assert dict_result_data['data'][0]['pid'] == '30'
                assert dict_result_data['data'][0]['pname'] == u'安徽'
        except requests.HTTPError,e:
            print e.message

