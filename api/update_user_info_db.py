# -*- coding: utf-8 -*-

from api import config_db as db
import datetime
import threading
import xlrd
import time

# 查询user_info数据库表用户信息
select_user_info = "select id,user_name,mobile_phone,id_card,authentication_status from user_info where mobile_phone ='{}' "
# 根据查询到的手机号更新user_info表中相关字段信息
update_user_info = "update user_info set user_name = '%s',id_card = '%s',authentication_status = '%d' where mobile_phone = '%s'"
# 向attachment表中插入相关ocr相关信息
insert_ocr_info = "insert into attachment(user_id,file_type,path_info,create_time,attachment_type,description) values ('%s','%d','%s','%s','%d','%s')"
# 信贷App OCR图片路径
xindai_ocr_img_path_info = "/export/data/img_server/credit-app/ocr/1535626496-2soME-a-0.png"
# 房贷APP OCR图片路径
fangdai_ocr_img_path_info = "/export/data/img_server/credit-app/ocrSecond/2019-07-11/1564026359-lRVwK-b-0.png"


# 查询node数据库中已注册成功的用户id信息
def query_mobile_info(host, phone):
    sql = select_user_info.format(phone)
    return db.db_base(host, sql)[0]['id']


# 更新user_info表中用户名，身份证，验证状态字段信息
def u_user_info(host, username, idcard, phone):
    sql = update_user_info % (username, idcard, 1, phone)
    db.db_base(host, sql)


# 获取当前时间，格式datetime格式
def get_local_time():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time


# 向node数据库表attachment插入身份证正面照片
def insert_ocr_front_info(host, phone, ocr_img_path_info):
    sql = insert_ocr_info % (query_mobile_info(host, phone), 1, ocr_img_path_info, get_local_time(), 1, 'front')
    db.db_base(host, sql)


# 向node数据库表attachment插入身份证反面照片
def insert_ocr_back_info(host, phone, ocr_img_path_info):
    sql = insert_ocr_info % (query_mobile_info(host, phone), 1, ocr_img_path_info, get_local_time(), 1, 'back')
    db.db_base(host, sql)


def user_handle(host, username, idcard, phone, ocr_img_path_info):
    try:
        u_user_info(host, username, idcard, phone)
        query_mobile_info(host, phone)
        insert_ocr_front_info(host, phone, ocr_img_path_info)
        insert_ocr_back_info(host, phone, ocr_img_path_info)
    except Exception as e:
        print("error_info:{}".format(str(e)))



if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=user_handle,
                          args=('161',
                                '宋贤',
                                '513436200907256117',
                                '13478795541',
                                fangdai_ocr_img_path_info))
    threads.append(t1)
    # t2 = threading.Thread(target=user_handle,
    #                       args=('161',
    #                             '陈玖',
    #                             '512222198310090038',
    #                             '13522110207',
    #                             fangdai_ocr_img_path_info))
    # threads.append(t2)
    # t3 = threading.Thread(target=user_handle,
    #                       args=('161',
    #                             '郭海福',
    #                             '513030198912256912',
    #                             '13522110208',
    #                             fangdai_ocr_img_path_info))
    # threads.append(t3)
    start = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
    stop = time.time()
    print("线程运行时间为：{}".format(stop - start))

