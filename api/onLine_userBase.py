# -*- coding: utf-8 -*-
'''
网销产品个人资料完善
'''
from api import readConfig as rc
from api import getHeaders as ah
from api import login as l
import requests
import json
import time



def getUserBase(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['getUserBase'])
    headers = ah.get_headers(host,phone,password)
    try:
        res = requests.post(url=url, headers=headers)
        return res.text
    except Exception as e:
        return "error_info: {}".format(str(e))



# 完善基本信息
def userBase(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['userBase'])
    headers = headers = ah.get_headers(host,phone,password)
    data = rc.read_json()['data']['userBaseData']
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "添加成功" in res.text:
            print("添加个人基本信息成功,个人基本信息内容如下：" + getUserBase(host, phone, password))
        else:
            print("错误信息为：" + res.text)
    except Exception as e:
        print("error_info: %s" %e)


def getOccupationInfo(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['getOccupationInfo'])
    headers = ah.get_headers(host,phone,password)
    try:
        res = requests.post(url=url, headers=headers)
        return res.text
    except Exception as e:
        return "error_info: {}".format(str(e))

# 完善职业类型
def perfectOccupation(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['occupation'])
    headers = ah.get_headers(host, phone, password)
    data = rc.read_json()['data']['occupationData']
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "添加成功" in res.text:
            print("用户职业信息添加成功,职业信息内容如下：" + getOccupationInfo(host, phone, password))
        # print("错误信息为：" + res.text)
    except Exception as e:
        print("error_info: {}".format(str(e)))


def getUserRelation(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['getUserRelation'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        return res.text
    except Exception as e:
        return "error_info: {}".format(str(e))


# 完善联系人信息
def userRelation(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['userRelation'])
    headers = ah.get_headers(host, phone, password)
    spouse = rc.read_json()['data']['userRelationData']['a']
    family = rc.read_json()['data']['userRelationData']['b']
    colleague = rc.read_json()['data']['userRelationData']['c']
    friend = rc.read_json()['data']['userRelationData']['d']
    contacts = "[{},{},{},{}]".format(spouse, family, colleague, friend)
    contacts = contacts.replace('\'', '\"').replace(' ', '')
    data = {"contacts": contacts,
            "emergencyContactKnow": rc.read_json()['data']['userRelationData']['emergencyContactKnow'],
            "familyKnow": rc.read_json()['data']['userRelationData']['familyKnow']
            }

    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "添加成功" in res.text:
            print("添加联系人信息成功，联系人信息如下：" + getUserRelation(host, phone, password))
        else:
            print("错误信息为：" + res.text)
    except Exception as e:
        print("Error_info:{}".format(str(e)))


# 获取运营商认证三方链接
def getMobileCertification(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['path']['onLineAuthMobileUrl'])
    headers = ah.get_headers(host, phone, password)
    data = {
        'type': '1'
    }
    try:
        res = requests.post(url=url, data=data, headers=headers)
        result = json.loads(res.text)
        if res.status_code == 200:
            print("获取网销运营商认证地址成功,地址内容如下：{}".format(result['url']))
        else:
            print("错误信息为：" + res.text)
    except Exception as e:
        print("Error_info:{}".format(str(e)))



# 完善用户个人资料信息及获取运营商认证链接
def perfectUserBaseInfo(host, phone, password):
    userBase(host, phone, password)
    perfectOccupation(host, phone, password)
    userRelation(host, phone, password)
    time.sleep(1)
    getMobileCertification(host, phone, password)


if __name__ == '__main__':
    host = str(input("请输入要运行的接口运行环境："))
    phone = str(input("请输入要执行的账号："))
    password = str(input("请输入要执行的账号密码："))
    perfectUserBaseInfo(host,phone,password)
