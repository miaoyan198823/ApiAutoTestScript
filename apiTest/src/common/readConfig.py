# -*- coding: utf-8 -*-
__author__ = 'miaoyan'



import configparser
import re

configPath = "D:/apiTest/src/config/config.ini"


class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_host(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_port(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_user(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_passwd(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_db(self,name):
        value = self.cf.get('DATABASE',name)
        return value

    def get_http(self,name):
        value = self.cf.get('URL',name)
        return value

    def get_Headers(self):
        self.headers = {}
        r = open('D:\\apiTest\\src\\config\\header.conf','r')
        headText = r.read()
        headers = re.split('\n',headText)
        for header in headers:
            result = re.split(':',header)
            self.headers[result[0]] = result[1]
        return self.headers









# if __name__ == '__main__':
#     r = ReadConfig()
#     print(r.get_http('login_url'))


