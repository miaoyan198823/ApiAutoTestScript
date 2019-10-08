# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import logging
import MySQLdb
from src.common import readConfig

localReadConfig = readConfig.ReadConfig()

class MyDB():
    global host,port,user,passwd,db,config
    host = localReadConfig.get_host('host')
    port = localReadConfig.get_port('port')
    user = localReadConfig.get_user('user')
    passwd = localReadConfig.get_passwd('passwd')
    db = localReadConfig.get_db('database')

    config = {
        'host':str(host),
        'port':int(port),
        'user':user,
        'passwd':passwd,
        'db':db

    }

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db = None
        self.cur = None


    def connectDB(self):
        try:
            self.conn = MySQLdb.connect(**config)
            self.cursor = self.conn.cursor()
            self.logger.info('DB connect successful!')
        except:
            self.logger.error('DB connect fail!')


    def executeSql(self,sql):
        self.connectDB()
        self.cursor.execute(sql)
        return self.cursor


    def get_all(self,cursor):
        value = cursor.fetchall()
        return value

    def get_one(self,cursor):
        value = cursor.fetchone()
        return value


    def db_close(self):
        self.conn.close()
        self.logger.info('close DB successful!')




if __name__=="__main__":
    DB = MyDB()
    DB.executeSql("select phoneNum,password from user where phoneNum = '15101183723'")









