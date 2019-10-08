# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import logging
import logging.config
import time
import os

logging.config.fileConfig("D:/apiTest/src/config/log.conf")
logger = logging.getLogger(__name__)


#定义系统当前时间
curTime = time.strftime('%Y%m%d%H%M%S',time.localtime())
#定义log文件输出格式按当前系统时间输出
logFile = os.path.abspath(os.path.join('D:/apiTest/src','log','log_{}.log'.format(curTime)))
handler = logging.handlers.RotatingFileHandler(logFile,maxBytes=4096000000,backupCount=9)
#重新传入日志格式
fmt = '[%(asctime)s](%(levelname)s)%(name)s : %(message)s'
formartter = logging.Formatter(fmt)
handler.setFormatter(formartter)
logger.addHandler(handler)






