#-*- coding:utf-8 -*-
import requests
from ddt import ddt,data,unpack
import unittest
class TesrWeiXinTag(unittest.TestCase):
    # @classmethod
    # def setyoClass(cls):
    #     print('类测试方法')
    #     print('初始化写在这里，数据库链接')

    # @classmethod
    # def tearDownClass(cls):
    #     print('类测试方法')
    #     print('销毁方法写在这里，例如断开数据库')
    #
    # def setUp(self):
    #     print('第一个测试方法前执行，准备共同数据，基础url')
    #
    # def test_method_01(self):
    #     self.assertEqual(1,1)
    #     self.assertNotEqual(1,2)
    #
    # def test_method_02(self):
    #     self.assertTrue(2>1)
    #     self.assertFalse(1>2)
    #     self.assertIn('lind','linda')
    @classmethod
    def setUpClass(cls):
        url = ' https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxf6d105886c9515a0&secret=84c045a0fbf89c453e2ec025edc854d0'
        rep = requests.get(url)
        cls.access_token = rep.json()['access_token']


    def test_create_tag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token='+self.access_token
        data = {
            "tag": {"name": "du" }
        }
        rep = requests.post(url=url, json=data)
        print(rep.json())
    def test_get_tag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/get?access_token='+self.access_token
        rep = requests.get(url=url)
        assert 2==rep.json()['tags'][0]['id']
        print(rep.json()['tags'][-1]['id'])
    #def test_update_tag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token='+self.access_token
        data={
            'id': 100, 'name': 'linda', 'count': 0
        }
        rep = requests.post(url=url,json=data)
        #assert 2 in rep.json()['tags'][0][id]
        assert 50 > rep.elapsed.total_seconds()
        print(rep.json())

    def del_text(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/delete?access_token='+self.access_token
        rep = requests.delete(url)
        assert 50 > rep.elapsed.total_seconds()
if __name__ == '__main__':
    unittest.main()

