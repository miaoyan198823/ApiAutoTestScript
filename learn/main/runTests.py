# -*- coding: utf-8 -*-
# @Time : 2019/9/6 16:11
# @Author : miaoyan

from public.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail



# sys.path.append("D:\workspace\learn")

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common = CommonUtil()
        self.send_email = SendEmail()



    #程序执行入口：
    def go_on_run(self):
        #统计通过用例数
        pass_count = []
        #统计失败用例数
        fail_count = []
        #取出Excel用例的总行数
        rows_count = self.data.get_case_line()
        #循环读取Excel表里各行列数据
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_request_data_for_json_keyword(i)
            headers = self.data.get_is_header(i)
            expect = self.data.get_expect_data(i)
            #如果该条用例需要执行，就执行接口方法
            if is_run:
                res = self.run_method.run_main(method, url, data, headers)
                #判断如果期望结果在实际结果中
                if self.common.is_contains(expect,res):
                    #则将实际结果写入实际结果里
                    self.data.write_result(i,"pass")
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)
        #发送测试结果邮件
        self.send_email.send_main(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()


