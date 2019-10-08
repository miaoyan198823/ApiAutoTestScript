# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getGoodsByCity_Sign


class GetGoodsByCityApi():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsByCity'
        params = getGoodsByCity_Sign.new_sign()
        headers = getGoodsByCity_Sign.get_headers()

    def test_getGoodsByCity_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['goods_id'] == '7448806'
                assert dict_result_data['data'][0]['product'] == u'伦巴萨59元2人餐'
                assert dict_result_data['data'][0]['title'] == u'[携程餐饮项目专用请不要修改]专用请不要修改专用请不要修改专用请不要修改一段曼妙时光'
                assert dict_result_data['data'][0]['short_title'] == u'伦巴萨意式餐厅：2-3人餐，知名商家'
                assert dict_result_data['data'][0]['sp_id'] == '5051050'
                assert dict_result_data['data'][0]['sales_city_id'] == '2419'
                assert dict_result_data['data'][0]['price'] == '59.00'
                assert dict_result_data['data'][0]['value'] == '130.00'
                assert dict_result_data['data'][0]['start_time'] == '2015-01-15 00:00:00'
                assert dict_result_data['data'][0]['deadline'] == '2018-09-10 00:00:00'
        except requests.HTTPError,e:
            print e.message



