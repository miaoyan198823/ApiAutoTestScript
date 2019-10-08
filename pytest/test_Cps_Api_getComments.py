# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import pytest
import getComments_Sign




class GetComments(object):
    def __init__(self):
        self.api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getComments'
        self.params = getComments_Sign.new_sign()
        self.headers = getComments_Sign.get_headers()

class TestGetComments(object):
    @pytest.fixture(scope='module')
    def gc(self):
        return GetComments()
        
    def test_getComments_api(self,gc):
        try:
            response = requests.get(gc.api_url,params=gc.params,headers=gc.headers,timeout=10)
            if response.status_code == 200:
                assert response.status_code == 200
                # print response.text.decode('unicode_escape')
                dict_result_data = json.loads(response.text)
                assert dict_result_data['data'][0]['user_name'] == u'm***92'
                assert dict_result_data['data'][0]['score'] == '5.0'
                assert dict_result_data['data'][0]['add_time'] == '2014-12-25 10:26:27'
                assert dict_result_data['data'][0]['content'] == u'真的不错.有机会还会去的'
        except requests.HTTPError,e:
            print e.message


