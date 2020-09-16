#-*- coding:utf-8 -*-
import pytest
'''
三个模块，查询不需要登陆，购物车，支付需要登陆
登陆是前提，不是测试。setup():写的登陆，必须所有模块都要登陆
UI自动化
'''

class TestHrm():

    @pytest.fixture(scope='module', autouse=True)
    def open_browser(self):

        print("打开浏览器，登陆")
        yield
        print("关闭浏览器")

    def login(self):
        print(self.driver)
        print("登陆")

    def test_search(self):
        print("admin")


    def test_cart(self):
        print("pim")


    def test_pay(self):
        print("job")
