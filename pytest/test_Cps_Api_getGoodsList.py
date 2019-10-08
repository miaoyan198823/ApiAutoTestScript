#coding=utf-8
__author__ = 'miaoyan'

import requests
import time
import hashlib
import json
import pytest
import getGoodsList_Sign


class GetGoodsList(object):
    def __init__(self):
        self.url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsList'
        self.params = getGoodsList_Sign.new_sign()
        self.headers = getGoodsList_Sign.get_headers()

class TestGetGoodsList(object):
    @pytest.fixture(scope='module')
    def gl(self):
        return GetGoodsList()

    def test_getGoodsList_api_api(self,gl):
        try:
            response = requests.get(gl.url,params=gl.params,headers=gl.headers,timeout=10)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['goods_id'] == '7448806'
                assert dict_result_data['data'][1]['sp_id'] == '5053514'
                assert dict_result_data['data'][0]['product'] == u'伦巴萨59元2人餐'
                assert dict_result_data['data'][0]['short_title'] == u'伦巴萨意式餐厅：2-3人餐，知名商家'
        except requests.HTTPError,e:
            print e.message

