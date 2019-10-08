# -*- coding: utf-8 -*-
# @Time : 2019/9/9 17:41
# @Author : miaoyan

import smtplib
from email.mime.text import MIMEText

class SendEmail:
    def __init__(self):
        self.mail_host = "smtp.163.com"
        self.send_user = "miaoyan_win@163.com"
        self.password = "miaoyan201256"

    def send_email(self,user_list,sub,content):
        user = "miaoyan" + "<" + self.send_user +">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['from'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(self.mail_host)
        server.login(self.send_user,self.password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num
        #通过率
        pass_result = "%.2f%%" %(pass_num/count_num*100)
        #失败率
        fail_result = "%.2f%%"%(fail_num/count_num*100)
        user_list = ['miaoyan@hexindai.com']
        sub = "接口测试用例汇总报告"
        content = "此次运行接口测试用例总数为{}个,\n 通过数为{}个,\n 通过率为{},\n 失败数为{}个,\n 失败率为{}\n".format(count_num,pass_num,pass_result,fail_num,fail_result)
        self.send_email(user_list,sub,content)




