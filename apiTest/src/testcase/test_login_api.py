# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import logging
import sys
import json
import unittest
from src.common import readConfig
from src.common import base


reload(sys)
sys.setdefaultencoding('utf8')

'''
调用base模块下读取Excel表格内接口参数信息以列表形式返回
对列表信息通过索引切片，然后用eval()方法将字符串转为字典
将字典dataALL赋给**DataALL
'''
testFile = 'txls_api_data.xlsx'
sheetName = 'login_api'
ALLData = base.get_data(testFile,sheetName)
dataALL = ALLData[1][2]
method = ALLData[1][1]

class TestLoginApi(unittest.TestCase):

    def setUp(self):
        '''
        导入readConfig模块，调取get_http()方法读取接口url地址
        :return:
        '''
        self.url = readConfig.ReadConfig().get_http('login_url')
        self.requestData = dataALL
        self.requestMethod = method
        self.logger = logging.getLogger(__name__)

    def test_login_api(self):
        '''
        调用base模块下对request的封装方法发送get请求
        :return:
        '''
        # headers = {'Content-Type':'application/json'}
        # params = {'phoneNum':'15101183723',
        #           'password':'2d44c7c724b5f1e17f6b8496268d5196'}
        # DataALL = {
        #     'params':params,
        #     'headers':headers
        # }
        try:
            DataALL = eval(self.requestData)
            res = base.get_request(self.url,self.requestMethod,**DataALL)
            # self.logger.info('request successful!')
            print json.dumps(res,indent=2)
        except Exception as e:
            self.logger.error('error info: %s'%e)


    def tearDown(self):
        pass



