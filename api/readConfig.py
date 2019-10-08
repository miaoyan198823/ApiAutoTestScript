# -*- coding: utf-8 -*-

import json
import os


#读取Json文件数据
file_path = os.path.dirname(os.path.realpath(__file__))
def read_json():
    with open("{}/data.json".format(file_path),'rb') as file_data:
        return json.load(file_data)

