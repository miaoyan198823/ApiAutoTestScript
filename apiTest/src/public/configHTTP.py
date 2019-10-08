# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import logging
import requests


class ConfigHttp(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)


    def getMethod(self,url,**DataALL):
        '''
        :param url: 接口url
        :param DataALL: get请求参数字典形式传递接口返回信息
        :return:get请求
        '''
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        try:
            response = requests.get(url,params=params,headers=headers)
            response.encoding = 'utf-8'
            text = response.json()
            return text
        except Exception as e:
            return self.logger.error('get request error:%s'%e)



    def postMethod(self,url,**DataALL):
        '''
        :param url: 接口url
        :param DataALL: post请求参数字典形式传递
        :return:post请求接口返回信息
        '''
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        data = DataALL.get('data')
        json = DataALL.get('json')
        try:
            response = requests.post(url,params=params,data=data,json=json,headers=headers)
            response.encoding='utf-8'
            text = response.json()
            return text
        except Exception as e:
            return self.logger.error('post request error: %s'%e)



    def patchMethod(self,url,**DataAll):
        headers = DataAll.get('headers')
        json = DataAll.get('json')
        try:
            response = requests.patch(url,json=json,headers=headers)
            response.encoding='utf-8'
            text = response.json()
            return text
        except Exception as e:
            return self.logger.error('patch request error %s'%e)





















