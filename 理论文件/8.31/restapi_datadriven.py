#-*- coding:utf-8 -*-
import unittest,requests
from ddt import ddt,file_data

@ddt
class TestRestApiDataDriven(unittest.TestCase):
    @file_data("testdata.yaml")
    def test_request_get_datadriven(self,**value):
        url=value['url']
        method=value['method']
        hearders=value['hearders']
        data=value['plyload']
        #print(rep.json())
        status_code = value['result']['status_code']
        rep = requests.request(method=method, headers=hearders, url=url,data=data)
        # delete 数据缺失，无法输出
        assert status_code == rep.status_code
        print(rep.json())
if __name__ == '__main__':
    unittest.main()