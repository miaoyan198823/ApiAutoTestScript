# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getGoods_Sign

class GetGoods(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoods'
        self.params = getGoods_Sign.new_sign()
        self.headers = getGoods_Sign.get_headers()

class TestGetGoods(object):
    @pytest.fixture(scope='module')
    def gs(self):
        return GetGoods()

    def test_getGoods_api(self,gs):
        try:
            response = requests.get(gs.api_url,params=gs.params,headers=gs.headers,timeout=10)
            if response.status_code == 200:
                # print response.text.decode('unicode_escape')
                assert response.status_code == 200
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data']['goods_id'] == '7448806'
                assert dict_result_data['data']['sp_id'] == '5051050'
                assert dict_result_data['data']['product'] == u'伦巴萨59元2人餐'
                assert dict_result_data['data']['title'] == u'[携程餐饮项目专用请不要修改]专用请不要修改专用请不要修改专用请不要修改一段曼妙时光'
                assert dict_result_data['data']['short_title'] == u'伦巴萨意式餐厅：2-3人餐，知名商家'
                assert dict_result_data['data']['sales_city_id'] == '2419'
                assert dict_result_data['data']['price'] == '59.00'
                assert dict_result_data['data']['value'] == '130.00'
                assert dict_result_data['data']['start_time'] == '2015-01-15 00:00:00'
                assert dict_result_data['data']['deadline'] == '2018-09-10 00:00:00'
        except requests.HTTPError,e:
            print e.message


