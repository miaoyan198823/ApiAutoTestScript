# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import sys
import json
import logging
import unittest
from nose.tools import assert_equal
from src.common import readConfig
from src.common import base


reload(sys)
sys.setdefaultencoding('utf8')

testFile = 'txls_api_data.xlsx'
sheetName = 'comments'
ALLData = base.get_data(testFile,sheetName)
dataAll = ALLData[1][2]
method = ALLData[1][1]

class TestComments(unittest.TestCase):
    def setUp(self):
        self.requestData = dataAll
        self.requestMethod = method
        self.logger = logging.getLogger(__name__)
        self.url = readConfig.ReadConfig().get_http('comments_url')


    def testCommentsApi(self):
        try:
            DataAll = eval(self.requestData)
            res = base.get_request(self.url,self.requestMethod,**DataAll)
            # print json.dumps(res,indent=2,sort_keys=True)
            return res
        except Exception as e:
            self.logger.error('error info:%s'%e)


    def testCheckResult(self):
        try:
            if self.testCommentsApi()['content'] == u'挺好':
                self.logger.info('check result successful!')
        except AssertionError as e:
            self.logger.error('check result error:%s'%e)



    def tearDown(self):
        pass





