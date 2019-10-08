# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getGoodsAddress_Sign

class GetGoodsAddress(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsAddress'
        self.params = getGoodsAddress_Sign.new_sign()
        self.headers = getGoodsAddress_Sign.get_headers()

class TestGetGoodsAddress(object):
    @pytest.fixture(scope='module')
    def ga(self):
        return GetGoodsAddress()

    def test_getGoodsAddress_api(self,ga):
        try:
            response = requests.get(ga.api_url,params=ga.params,headers=ga.headers,timeout=10)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['fd_id'] == '511681'
                assert dict_result_data['data'][0]['telephone'] == '4006123277'
                assert dict_result_data['data'][0]['lng'] == '116.40733'
                assert dict_result_data['data'][0]['lat'] == '40.00677'
                assert dict_result_data['data'][0]['address'] == u'北京朝阳区慧忠北里京师科技大厦2层'
                assert dict_result_data['data'][0]['fd_name'] == u'爱康国宾 （北京亚运村慧忠北里体检分院）'
                assert dict_result_data['data'][0]['shop_hours'] == '08:00-24:00'
                assert dict_result_data['data'][0]['circle_name'] == u'亚运村'
                assert dict_result_data['data'][0]['&getCity']['city_name'] == u'北京'
                assert dict_result_data['data'][0]['&getCity']['pname'] == u'北京'
                assert dict_result_data['data'][0]['circle_name'] == u'亚运村'
                assert dict_result_data['data'][0]['&getGoodsDistrict']['district_name'] == u'朝阳'
                assert dict_result_data['data'][0]['&getGoodsDistrict']['district_py'] == 'chaoyang'
        except requests.HTTPError,e:
            print e.message
