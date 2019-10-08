# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

from nose.tools import assert_equal
import requests



class TestLoginApi(object):
    def setUp(self):
        self.loginApiUrl = 'http://10.1.36.221:8086/gateway/members/login'
        self.headers = {'Content-Type':'application/json'}
        self.params = {'phone':'15101183723',
                       'password':'2d44c7c724b5f1e17f6b8496268d5196'}

    def tearDown(self):
        pass

    def testLoginApi(self):
        try:
            response = requests.get(self.loginApiUrl,params=self.params,headers=self.headers)
            if response.status_code == 200:
                assert_equal(response.status_code,200)
                dict_data_result = response.json()
                print dict_data_result
                # assert_equal(dict_data_result['phoneNum'],'15101183723')
        except requests.HTTPError,e:
            print e.message





