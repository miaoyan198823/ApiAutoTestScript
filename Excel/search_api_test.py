# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import json
import unittest

class SearchApiTest(unittest.TestCase):
    def setUp(self):
        self.search_api_url = 'http://api7.mobile.lashou.com/lashou.php/Search/search'
        self.headers = {'debug':'true',
                        'cache':'false',
                        'webtime':'1464057254',
                        'traceinfo':'userid=8DBE140ACCF14D93;versionname=7.25;versioncode=7.25;buildversion=201605240921-72;osversion=9.3.1;model=iPhone7,2;appname=groupbuy;clientname=iphone;channelid=10000;cityid=2419;idfa=B1D95B2C-EAEC-467B-A9AF-ADBBFEAAD41F;clientid=b84e43636ab2058d94c3667049995e39c7bab4fc;location=116.483252,40.006940;network=WIFI;seq=b84e43636ab2058d94c3667049995e39c7bab4fc0112;num=b84e43636ab2058d94c3667049995e39c7bab4fc-1463712168'}
        self.params = {"sign":"917ce0ff426f121335e46ef6d7f9ced8",
                       "time":"1464057253",
                       "params":{"keyword":"电影","category":"0","sort_type":"4","district_id":"0","zone_id":"0","longitude":"116483252.","latitude":"40.006940","user_id":"0","city_id":"2419","offset":"0","force_update":"0","page_size":"20"}}
        self.data = json.dumps(self.params)

    def test_get_search_api_posts_data(self):
        try:
            response = requests.post(self.search_api_url,data=self.data,headers=self.headers)
            print response.text.decode('unicode_escape')
        except requests.HTTPError,e:
            print e.message


    def test_status_code_200(self):
        r = requests.post(self.search_api_url,data=self.data,headers=self.headers)
        if r.status_code == 200:
            print(r.status_code)
            return True

    def test_assert_search_response_data(self):
        r_post = requests.post(self.search_api_url,data=self.data,headers=self.headers)
        dict_data_result = json.loads(r_post.text)
        self.assertEqual(dict_data_result['ret'],10000)
        self.assertEqual(dict_data_result['msg'],u'成功')
        self.assertEqual(dict_data_result['result']['page_size'],20)

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()

