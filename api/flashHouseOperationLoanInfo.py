# -*- coding: utf-8 -*-
# @Time : 2019/4/19 11:03
# @Author :缪岩
#闪房经营贷信息完善

from api import readConfig as rc
from api import getHeaders as ah
from api import flashHouseLoanInfo as fh
import requests
import time


# 完善闪房经营贷个人资料基本信息
def save_customer_house_manageMent_info(host, phone, password):
    fh.save_CustomerForHouseLoan(host, phone, password)


# 完善闪房经营贷经营信息
def save_customer_manageMent_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['customerManageMentInfo'])
    headers = ah.get_headers(host, phone, password)
    data = rc.read_json()['data']['cutomerMangeMentInfo']
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if "success" in res.text:
            print("添加经营信息成功,经营信息内容如下：" + get_customer_manageMent_info(host, phone, password))
        else:
            print("接口异常信息为：" + res.text)
    except Exception as e:
        print("error_info:%s" % e)


# 获取闪房经营贷经营信息
def get_customer_manageMent_info(host, phone, password):
    url = "{}{}".format(rc.read_json()['url'][str(host)], rc.read_json()['houseLoanPath']['getCustomerManageMentInfo'])
    headers = ah.get_headers(host, phone, password)
    try:
        res = requests.post(url=url, headers=headers)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        return "error_info:{}".format(e)


# 完善闪房经营贷房产基本信息
def save_house_manageMent_base_info(host, phone, password):
    fh.save_house_base_info(host, phone, password)


# 添加闪房经营贷共有产权人
def save_property_manageMent_holder_info(host, phone, password):
    fh.save_property_holder_info(host, phone, password)


def main(host, phone, password):
    save_customer_house_manageMent_info(host, phone, password)
    save_customer_manageMent_info(host, phone, password)
    fh.get_house_auth_mobile_url(host,phone,password)
    time.sleep(2)
    save_house_manageMent_base_info(host, phone, password)


if __name__ == '__main__':
    host = str(input("请输入要运行的接口运行环境："))
    phone = str(input("请输入要执行的账号："))
    password = str(input("请输入要执行的账号密码："))
    main(host,phone,password)
