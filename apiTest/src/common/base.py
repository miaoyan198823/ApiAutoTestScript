# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


from src.public import configHTTP
from src.public import readExcel


def get_request(url,method,**DataALL):
    '''
    对configHTTP文件 get post方法进行二次封装
    :param url: 接口url
    :param method: request 请求方式
    :param DataALL: 接口请求参数字典形式传递
    :return:接口返回信息
    '''
    if method == 'get':
        response = configHTTP.ConfigHttp().getMethod(url,**DataALL)
    elif method == 'post':
        response = configHTTP.ConfigHttp().postMethod(url,**DataALL)
    elif method == 'patch':
        response = configHTTP.ConfigHttp().patchMethod(url,**DataALL)
    return response



def get_data(testFile,sheetName):
    '''
    对readExcel文件内方法进行二次封装
    :param testFile: Excel文件存放路劲
    :param sheetName: sheetName
    :return:返回当前sheet下内容
    '''
    dataInfo = readExcel.ExcelDataInfo(r'D:\apiTest\src\config\testData\%s'%testFile)
    Data = dataInfo.get_sheetInfo_by_name(sheetName)
    return Data





