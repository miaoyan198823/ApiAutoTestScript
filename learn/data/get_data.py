# -*- coding: utf-8 -*-
# @Time : 2019/9/6 14:05
# @Author : miaoyan


from util import operation_excel
from data import data_config
from util import operation_json
from util import operation_header

class GetData:
    def __init__(self):
        self.opera_excel = operation_excel.OperationExcel()
        self.opera_json = operation_json.OperationJson()
        self.opera_header = operation_header


    #获取case个数
    def get_case_line(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = data_config.get_is_run()
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    #从Json文件中获取headers信息
    def get_headers(self):
        headers = self.opera_json.get_keywords('headersData')
        headers['Authorization'] = self.opera_header.get_token()
        return headers

    #获取是否携带header
    def get_is_header(self,row):
        col = data_config.get_is_header()
        headers = self.opera_excel.get_cell_value(row,col)
        if headers == "yes":
            return self.get_headers()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = data_config.get_request_method()
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取请求url
    def get_request_url(self,row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell_value(row,col)
        return url


    #获取请求数据
    def get_request_data_for_excel(self,row):
        col = data_config.get_request_data()
        request_data_info = self.opera_excel.get_cell_value(row,col)
        if request_data_info == '':
            return None
        return request_data_info

    #通过Excel文件关键字获取存放参数的Json文件数据
    def get_request_data_for_json_keyword(self,row):
        data = self.opera_json.get_keywords(self.get_request_data_for_excel(row))
        return data

    #获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == "":
            return None
        return expect

    #写入实际结果
    def write_result(self,row,value):
        col = data_config.get_result()
        self.opera_excel.write_value(row,col,value)





