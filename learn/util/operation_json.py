# -*- coding: utf-8 -*-
# @Time : 2019/9/6 11:07
# @Author : miaoyan


import json


class OperationJson(object):
    def __init__(self,file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = r'D:\workspace\learn\data\data.json'
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_name,'rb') as f:
            data = json.load(f)
        return data


    #获取Json文件某个字段信息
    def get_keywords(self,keyword):
        return self.data[keyword]

