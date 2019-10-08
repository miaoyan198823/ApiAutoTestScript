# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import logging
import sys
import json
import unittest
from nose.tools import assert_equal
from src.common import readConfig
from src.common import base


reload(sys)
sys.setdefaultencoding('utf8')


testFile = 'txls_api_data.xlsx'
sheetName = 'sceneAccountState'
AllData = base.get_data(testFile,sheetName)
dataALL = AllData[1][2]
method = AllData[1][1]

class TestSceneAccountApi(unittest.TestCase):
    def setUp(self):
        self.requestData = dataALL
        self.requestMethod = method
        self.url = readConfig.ReadConfig().get_http('sceneAccountState_url')
        self.logger = logging.getLogger(__name__)


    def testSceneAccountApi(self):
        '''

          headers = {
            'guid':'80b5c1ca-ea89-4221-a30f-19c6b42537fc',
            'Content-Type':'application/json'
        }

        json = {
            "id": "42098077ce51418f",
            "status": "pass"
        }

        DataAll = {
            'json':json,
            'headers':headers
        }
        '''


        try:
            DataAll = eval(self.requestData)
            res = base.get_request(self.url,self.requestMethod,**DataAll)
            # print json.dumps(res,indent=2,sort_keys=True)
            return res
        except Exception as e:
            self.logger.error('error info:%s'%e)

    def testCheckRusult(self):
        try:
            assert_equal(self.testSceneAccountApi()['status'],'pass')
            self.logger.info('check result successful!')
        except Exception as e:
            self.logger.error('check result error:%s'%e)


    def tearDown(self):
        pass



















