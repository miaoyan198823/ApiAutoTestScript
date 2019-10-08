# -*- coding: utf-8 -*-
# @Time : 2019/9/6 10:25
# @Author : miaoyan

import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self,file_name = None,sheet_id = None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = r'D:\workspace\learn\data\api_data.xls'
            self.sheet_id = 0  #默认第一个sheet
        self.data = self.get_data()

    #获取sheet数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某个单元格
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)


