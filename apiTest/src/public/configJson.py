# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import json


class ConfigJson(object):
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'D:/apiTest/src/config/testData/follow.json'
        else:
            self.file_path = file_path
        self.data = self.read_json()


    #读取json文件
    def read_json(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
        return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]


if __name__ == "__main__":
    c = ConfigJson()
    print c.read_json(r'D:\apiTest\src\config\testData\follow.json')


