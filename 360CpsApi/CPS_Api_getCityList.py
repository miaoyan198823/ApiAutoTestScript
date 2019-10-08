# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import time
import unittest
import getCityList_Sign


class GetCityList():
    def __init__(self):
        global api_url
        global params
        global headers
        api_url = 'http://wireless.api.test.lashou.com/index4openapi.php/Openapi/Method/getCityList'
        params = getCityList_Sign.new_sign()
        headers = getCityList_Sign.get_headers()

    def test_getCityList_api(self):
        try:
            response = requests.get(api_url,params=params,headers=headers,timeout=2)
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

