#coding=utf-8
__author__ = 'miaoyan'

import requests
import time
import hashlib
import json
import unittest
import getGoodsList_Sign


class GetGoodsList():

    def __init__(self):
        global url
        global params
        global headers
        url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsList'
        params = getGoodsList_Sign.new_sign()
        headers = getGoodsList_Sign.get_headers()

    def test_getGoodsList_api_api(self):
        try:
            response = requests.get(url,params=params,headers=headers,timeout=2)
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

