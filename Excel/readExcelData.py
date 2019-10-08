# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import xlrd
import requests
import sys
import json


reload(sys)
sys.setdefaultencoding('utf-8')


fileName = r'E:/123.xls'
def api_response_code(url,params,headers):
    response = requests.post(url,params,headers)
    code = response.status_code
    return code

def api_response_text(url,params,headers):
    response = requests.post(url,params,headers)
    return response.text

def readExcelDate(fileName):
    try:
        book = xlrd.open_workbook(fileName)
        table = book.sheets()[0]
        rows = table.nrows
        # api_list = []
        for row in range(1,rows):
            api_url = table.row_values(row)[0]
            api_params = table.cell(row,1).value
            api_headers = table.cell(row,2).value
            ex_code = table.cell(row,3).value
            # api_list.append(api_url)
            # print api_list
            ac_code = api_response_code(url=api_url,params=json.dumps(eval(api_params)),headers=api_headers)
            if ac_code == ex_code:
                print "pass"
            ac_response_text = api_response_text(url=api_url,params=json.dumps(eval(api_params)),headers=api_headers)
            print ac_response_text.decode('unicode_escape')
    except Exception,e:
        print str(e)

if __name__=="__main__":
    readExcelDate(fileName)