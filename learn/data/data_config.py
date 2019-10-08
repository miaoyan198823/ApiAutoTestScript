# -*- coding: utf-8 -*-
# @Time : 2019/9/6 11:40
# @Author : miaoyan

from util import operation_json

class Global_val:
    #case_id列数
    id = 0
    #host
    url = 2
    #请求方式
    request_method = 3
    #请求header
    header = 4
    #请求数据
    request_data = 8
    #预期结果
    expect = 9
    #实际结果
    result = 10
    #是否执行
    is_run = 11


def get_id():
    return Global_val.id

def get_url():
    return Global_val.url

def get_request_method():
    return Global_val.request_method

def get_is_header():
    return Global_val.header

def get_request_data():
    return Global_val.request_data

def get_expect():
    return Global_val.expect

def get_result():
    return Global_val.result

def get_is_run():
    return Global_val.is_run

