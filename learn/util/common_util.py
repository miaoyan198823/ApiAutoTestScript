# -*- coding: utf-8 -*-
# @Time : 2019/9/9 10:26
# @Author : miaoyan



class CommonUtil:
    def is_contains(self,str_one,str_two):
        '''
        判断一个字符串是否在另外一个堆字符串中
        str_one:查找的字符串
        str_two:被查找的一堆字符串
        :return:
        '''
        flag = None
        if str(str_one) in str(str_two):
            flag = True
        else:
            flag = False
        return flag


