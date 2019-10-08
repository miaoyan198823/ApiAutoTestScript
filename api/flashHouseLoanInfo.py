# -*- coding: utf-8 -*-
'''
闪房贷基础资料信息
author：缪岩
'''
from api import readConfig as rc
from api import getHeaders as ah
import requests
import json
import time


# 完善闪房贷个人资料基本信息
def save_CustomerForHouseLoan(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['CustomerForHouseLoan'])
    headers = ah.get_headers(host, phone, password)
    link1 = rc.read_json()['data']['linkMen']["a"]
    link2 = rc.read_json()['data']['linkMen']["b"]
    link3 = rc.read_json()['data']['linkMen']["c"]
    link4 = rc.read_json()['data']['linkMen']["d"]
    linkMen = "[{},{},{},{}]".format(link1, link2, link3, link4)
    linkMen = linkMen.replace('\'', '\"').replace(' ', '')
    data = rc.read_json()['data']['houseloan_couserInfo']
    data['linkMen'] = linkMen
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            print("添加基本信息成功,基本信息内容如下：" + get_customer_info(host, phone, password))
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:{}".format(str(e)))


# 获取闪房贷个人资料基本信息
def get_customer_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getCustomerInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        return res.text
    except Exception as e:
        return "error_info:{}".format(str(e))


# 完善闪房贷个人资料工作信息
def save_custome_work_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['customerWorkInfo'])
    headers = ah.get_headers(host, phone, password)
    data = rc.read_json()['data']['customerWorkInfo']
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            print("添加工作信息成功,工作信息内容如下：" + get_customer_work_info(host, phone, password))
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:{}".format(str(e)))


# 获取闪房贷个人资料工作信息
def get_customer_work_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getCustomerWorkInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        return res.text
    except Exception as e:
        return "error_info: {}".format(str(e))


# 获取房产基本信息参数ID值
def get_house_base_info_id(host, phone, password):
    url = url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getBaseHouseInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        if "success" in res.text:
            info = json.loads(res.text)
            id = info['houseBaseInfo']['id']
            return id
        else:
            return res.text
    except Exception as e:
        return "error_info:{}".format(str(e))


# 完善闪房贷房产基本信息
def save_house_base_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['houseBaseInfo'])
    headers = ah.get_headers(host, phone, password)
    data = rc.read_json()['data']['houseloanBaseInfo']
    data['id'] = get_house_base_info_id(host, phone, password)
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            print("添加房产基本信息成功,房产基本信息内容如下：" + get_house_base_info(host, phone, password))
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:{}".format(str(e)))


# 获取闪房贷房产基本信息
def get_house_base_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getBaseHouseInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        if "success" in res.text:
            return res.text
    except Exception as e:
        return "error_info:{}".format(str(e))


# 添加闪房贷共有产权人
def save_property_holder_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['propertyHolderInfo'])
    headers = ah.get_headers(host, phone, password)
    data = rc.read_json()['data']['propertyHodlerInfo']
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            print("添加共有产权人信息成功,共有产权人信息内容如下：" + get_property_hodler_info(host, phone, password))
    except Exception as e:
        print("error_info:{}".format(str(e)))


# 获取闪房贷共有产权人信息
def get_property_hodler_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getPropertyHolderInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        if "success" in res.text:
            return res.text
    except Exception as e:
        return "error_info:{}".format(str(e))


# 获取房贷运营商认证url地址
def get_house_auth_mobile_url(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['houseLoanAuthMobileUrl'])
    headers = ah.get_headers(host, phone, password)
    data = {
        'type': '1'
    }
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            url_info = json.loads(res.text)
            print("获取房贷运营商认证地址成功,地址内容如下:" + url_info['url'])
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:{}".format(str(e)))

def main(host, phone, password):
    save_CustomerForHouseLoan(host, phone, password)
    save_custome_work_info(host, phone, password)
    get_house_auth_mobile_url(host, phone, password)
    time.sleep(2)
    save_house_base_info(host, phone, password)


if __name__ == '__main__':
    host = str(input("请输入要运行的接口运行环境："))
    phone = str(input("请输入要执行的账号："))
    password = str(input("请输入要执行的账号密码："))
    main(host,phone,password)