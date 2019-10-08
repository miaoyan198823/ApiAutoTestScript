# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import logging
import unittest
from src.common import readConfig
from src.common import base



testFile = 'txls_api_data.xlsx'
sheetName = 'yxindex'
AllData = base.get_data(testFile,sheetName)
dataALL = AllData[1][2]
method = AllData[1][1]


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.url = readConfig.ReadConfig().get_http('yxinde_url')
        self.requestData = dataALL
        self.requestMethod = method
        self.logger = logging.getLogger(__name__)


    def test_search_api(self):
        try:
            DataALL = eval(self.requestData)
            res = base.get_request(self.url,self.requestMethod,**DataALL)
            print res
        except Exception as e:
            print(self.logger.error('error info: %s'%e))


    def tearDown(self):
        pass











