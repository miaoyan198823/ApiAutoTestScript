# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getGoodsScore_Sign

class GetGoodsScore(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getGoodsScore'
        self.params = getGoodsScore_Sign.new_sign()
        self.headers = getGoodsScore_Sign.get_headers()

class TestGetGoodsScore(object):
    @pytest.fixture(scope='module')
    def gs(self):
        return GetGoodsScore()

    def test_getGoodsScore_Api(self,gs):
        try:
            response = requests.get(gs.api_url,params=gs.params,headers=gs.headers,timeout=10)
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

