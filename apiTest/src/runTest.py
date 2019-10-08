# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import unittest
import time
import HTMLTestRunner


if __name__=="__main__":
    test_dir = "./testcase"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now = time.strftime("%Y-%m-%d-%H-%M",time.localtime(time.time()))
    filename ='./result/'+ now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='TXLS Api Test Report',
                                           description='TXLS Group')
    runner.run(discover)
    fp.close()

