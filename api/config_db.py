# -*- coding: utf-8 -*-

import pymysql
from api import readConfig

def db_base(host,sql):
    db_conn = pymysql.connect(
        host=str(readConfig.read_json()['database'][host]['host']),
        port=int(readConfig.read_json()['database'][host]['port']),
        user=readConfig.read_json()['database'][host]['user'],
        passwd=readConfig.read_json()['database'][host]['password'],
        db=readConfig.read_json()['database'][host]['db'],
        cursorclass = pymysql.cursors.DictCursor
    )
    cursor = db_conn.cursor()
    try:
        cursor.execute(sql)
        db_conn.commit()
        data = cursor.fetchall()
        return data
    except:
        db_conn.rollback()
    db_conn.close()
















