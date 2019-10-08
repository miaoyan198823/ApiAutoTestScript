# -*- coding: utf-8 -*-
# @Time : 2019/9/6 15:48
# @Author : miaoyan

import requests
import json

class RunMethod:
    def post_main(self,url,data,headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url,data=data,headers=headers).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res


    def get_main(self,url,data=None,headers=None):
        res = None
        if headers != None and data != None:
            res = requests.get(url=url,data=data,headers=headers).json()
        elif headers != None:
            res = requests.get(url=url,headers=headers).json()
        return res


    def run_main(self,method,url,data=None,headers=None):
        res = None
        if method == "POST":
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)


