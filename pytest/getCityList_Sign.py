# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import hashlib
import time

secret='84a34cb2cc1b931fe83de9a7e6df7e5fbd4421f33667ecc7f0c15e64e7b94563'
dict_get_cityList = {'client':'e22c59101699ac978ee83bfb81d4c949','time':'1464340958','page':1,'per_page':5}

#生成时间戳
def get_time():
    time_data = time.time()
    return int(time_data)

def get_sign(dict_get_cityList,secret):

    sourt_dict = sorted(dict_get_cityList.items(),key=lambda d:d[0])

    s=''
    for d in sourt_dict:
        s += str(d[0])
        s += str('=')
        s += str(d[1])
    s+=secret

    sign = hashlib.md5()
    sign.update(s)
    mySign = sign.hexdigest()
    return mySign

def get_headers():
    headers = {'debug':'true',
               'cache':'false',
               'webtime':'1463452829',
               'traceinfo':'userid=8DBE140ACCF14D93;versionname=7.25;versioncode=7.25;buildversion=201605240921-72;osversion=9.3.1;model=iPhone7,2;appname=groupbuy;clientname=iphone;channelid=10000;cityid=2419;idfa=B1D95B2C-EAEC-467B-A9AF-ADBBFEAAD41F;clientid=b84e43636ab2058d94c3667049995e39c7bab4fc;location=116.483252,40.006940;network=WIFI;seq=b84e43636ab2058d94c3667049995e39c7bab4fc0112;num=b84e43636ab2058d94c3667049995e39c7bab4fc-1463712168'}
    return headers

def new_sign():
    dict_get_cityList['time'] = get_time()
    dict_get_cityList['sign'] = get_sign(dict_get_cityList,secret)
    return dict_get_cityList
