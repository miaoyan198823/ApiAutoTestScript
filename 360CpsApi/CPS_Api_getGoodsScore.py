# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getGoodsScore_Sign

class GetGoodsScore():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsScore'
        params = getGoodsScore_Sign.new_sign()
        headers = getGoodsScore_Sign.get_headers()

    def test_getGoodsScore_Api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data']['total_avg'] == '5.0'
                assert dict_result_data['data']['comment_num'] == 8
                assert dict_result_data['data']['total_percent'] == '100%'
                assert dict_result_data['data']['score_percent']['five'] == '100%'
        except requests.HTTPError,e:
            print e.message

