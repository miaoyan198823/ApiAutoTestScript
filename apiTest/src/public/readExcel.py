# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import xlrd
from xlutils import copy


class ExcelDataInfo(object):
    def __init__(self,path = ''):
        '''
        :param path: Excel文件路径
        :return:操作Excel对象
        '''
        self.xl = xlrd.open_workbook(path)


    def get_sheetInfo_by_name(self,name):
        '''
        :param name: Excel sheetNama
        :return: 当前sheet内容
        '''
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheet_info(self):
        '''
        :return:返回当前sheet下所有行的内容
        '''
        infoList = []
        for row in range(0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            infoList.append(info)
        return infoList



class OperationExcel(object):
    def __init__(self,file_name = None,sheet_id = None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id

        else:
            self.file_name = r'D:\apiTest\src\config\testData\txls_api_data.xlsx'
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
    def wirte_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
















# if __name__ == "__main__":
#     e = ExcelDataInfo(r'D:\apiTest\src\config\testData\txls_api_data.xlsx')
#     print(e.get_sheetInfo_by_name('login_api'))

