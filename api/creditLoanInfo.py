# -*- coding: utf-8 -*-
# @Time : 2019/4/22 10:58
# @Author : miaoyan

'''
信贷产品基本信息完善
'''

from api import onLine_userBase as ol
from api import readConfig as rc
from api import getHeaders as ah
import requests
import json



#获取三方运营商页面URL地址
def get_credit_mobile_authUrl(host,phone,password):
    url = "{}{}".format(rc.read_json()['url'][str(host)],rc.read_json()['path']['creditAuthMobileUrl'])
    headers = ah.get_headers(host,phone,password)
    data = {
        'type':'1'
    }
    try:
        res = requests.post(url=url,data=data,headers=headers)
        if res.status_code == 200:
            result = json.loads(res.text)
            print("获取信贷运营商认证ULR地址成功，地址如下：{}".format(result['url']))
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:{}".format(str(e)))


#完善信贷基本信息
def main(host,phone,password):
    ol.userBase(host,phone,password)
    ol.perfectOccupation(host,phone,password)
    ol.userRelation(host,phone,password)
    get_credit_mobile_authUrl(host,phone,password)


if __name__ == '__main__':
    host = str(input("请输入要运行的接口运行环境："))
    phone = str(input("请输入要执行的账号："))
    password = str(input("请输入要执行的账号密码："))
    main(host,phone,password)







