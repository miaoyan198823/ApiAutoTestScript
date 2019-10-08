# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import time
import CPS_Api_getCity
import CPS_Api_getCityList
import CPS_Api_getComments
import CPS_Api_getCpsBill
import CPS_Api_getCpsStatistics
import CPS_Api_getGoods
import CPS_Api_getGoodsAddress
import CPS_Api_getGoodsByCity
import CPS_Api_getGoodsList
import CPS_Api_getGoodsScore

t = 3
#获取某个城市的名称或者省份接口
CPS_Api_getCity.GetCiytApi().test_getCity_api()
time.sleep(t)
#获取所有城市的名称或者省份接口
CPS_Api_getCityList.GetCityList().test_getCityList_api()
time.sleep(t)
#获取团单的评论列表接口
CPS_Api_getComments.GetCommentsApi().test_getComments_api()
time.sleep(t)
#获取CPS账单
CPS_Api_getCpsBill.GetCpsBill().test_getCpsBill_api()
time.sleep(t)
#获取当前CPS账单统计接口
CPS_Api_getCpsStatistics.GetCpsStatistics().test_getCpsStatistics_api()
time.sleep(t)
#获取某个团单接口
CPS_Api_getGoods.GetGoodsApi().test_getGoods_api()
time.sleep(t)
#获取某团单的地址列表接口
# CPS_Api_getGoodsAddress.GetGoodsAddressApi().test_getGoodsAddress_api()
time.sleep(t)
#获取某个城市的团单接口
CPS_Api_getGoodsByCity.GetGoodsByCityApi().test_getGoodsByCity_api()
time.sleep(t)
#获取团单列表接口
CPS_Api_getGoodsList.GetGoodsList().test_getGoodsList_api_api()
time.sleep(t)
#获取某团单的评分接口
CPS_Api_getGoodsScore.GetGoodsScore().test_getGoodsScore_Api()




