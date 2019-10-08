# -*- coding: utf-8 -*-

from api import readConfig
from api import login
import requests
import os
import json
from api import getHeaders as gh
import time
import threading

def get_auth_code(host,phone):
    url = "{}{}".format(readConfig.read_json()['url'][str(host)],readConfig.read_json()['path']['authcode'])
    data = {'phone':phone}
    res = requests.post(url=url,data=data)
    if '{"interval":120}' in res.text:
        print("获取验证码成功！")
    else:
        print(res.text)


def register(host,phone,password):
    url = "{}{}".format(readConfig.read_json()['url'][str(host)],readConfig.read_json()['path']['register'])
    data ={
        'phone':str(phone),
        'password':str(password),
        'captcha':'888888',
        'login_termianl':'2'
    }
    res = requests.post(url =url,data=data)
    if 'access_token' and 'token_type' in res.text:
        auth = "{} {}".format(res.json()['token_type'].capitalize(),res.json()['access_token'])
        print("账户注册成功,返回Token为：%s" %(auth))
    else:
        print(res.text)

def manager(host,phone,password,customer_code):
    path1 = '{}'.format(readConfig.read_json()['url'][str(host)])
    path2 = '/v1/staff/{}?nothing=' .format(customer_code)
    url1 = path1 + path2
    path3 = '{}'.format(readConfig.read_json()['path']['staff'])
    url2 = path1 + path3
    headers = readConfig.read_json()['headers']
    headers['Authorization'] = login.login(host,phone,password)
    res1 = requests.get(url=url1,headers=headers)
    data = {
        'staffNo':customer_code
    }
    res2 = requests.post(url=url2,data=data,headers=headers)
    mess = '{}\n{}'.format(res1.json(),res2.json())
    if 'hasStaffServer' in mess:
        print(mess)

def face_ocr(host,phone,password):
    url = "{}{}".format(readConfig.read_json()['url'][str(host)],readConfig.read_json()['path']['ocr'])
    headers = {"Connection": "keep-alive", "Host": "api-sandbox.hxgp.com"}
    headers['Authorization'] = login.login(host,phone,password)
    ocr_img_path = os.path.abspath(os.path.dirname(__file__))
    with open('{}\\1.jpg'.format(ocr_img_path),'rb') as frontImage:
        with open('{}\\2.jpg'.format(ocr_img_path),'rb') as backImage:
            files = {
                'frontImage':frontImage,
                'backImage':backImage
            }
            try:
                res = requests.post(url=url,headers=headers,files=files)
                result = json.loads(res.text)
                if 'idCardCode' and 'idCardName' in result:
                    print("OCR识别成功,识别结果为 ：{}".format(res.text))
                else:
                    print("OCR识别成功,接口错误信息为：{}".format(res.text))
            except Exception as e:
                print("error_info:{}".format(str(e)))

def confirmation(host,idCard,idCardName,phone,password):
    url = "{}{}".format(readConfig.read_json()['url'][str(host)],readConfig.read_json()['path']['confirmation'])
    headers = gh.get_headers(host,phone,password)
    data = {
        'confirmation':1,
        'idCardCode':idCard,
        'idCardName':idCardName
    }
    try:
        res = requests.post(url=url,data=data,headers=headers)
        result = json.loads(res.text)
        if res.status_code == 200:
            print("实名认证通过,接口返回内容为:{}".format(result))
        else:
            print("实名认证失败,接口错误信息为：{}".format(res.text))
    except Exception as e:
        print("error_info:{}".format(str(e)))


def register_all(host,phone,password,idCard,idCardName):
    get_auth_code(host,phone)
    register(host,phone,password)
    face_ocr(host,phone,password)
    confirmation(host,idCard,idCardName,phone,password)
    # db.user_handle(host, phone, username, idcard, ocr_img_path_info)
    # manager(host,phone,password,customer_code)







if __name__ == '__main__':
    host = str(input("请输入要运行的接口运行环境："))
    phone = str(input("请输入注册账号："))
    password = str(input("请输入注册账号密码："))
    idCard = str(input("请输入用户姓名："))
    idCardName = str(input("请输入用户身份证号："))
    register_all(host,phone,password,idCard,idCardName)

    # threads = []
    # t1 = threading.Thread(target=register_all,
    #                       args=('161',
    #                             '13522110206',
    #                             '123123123'))
    # threads.append(t1)
    # t2 = threading.Thread(target=register_all,
    #                       args=('161',
    #                             '13522110207',
    #                             '123123123'))
    # threads.append(t2)
    # t3 = threading.Thread(target=register_all,
    #                       args=('161',
    #                             '13522110208',
    #                             '123123123'))
    # threads.append(t3)
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #     t.join()


