#-*- coding:utf-8 -*-
import pytest
from selenium import webdriver
import unittest, time, re,os
'''
三个模块，查询不需要登陆，购物车，支付需要登陆
登陆是前提，不是测试。setup():写的登陆，必须所有模块都要登陆
UI自动化
'''

class TestHrm():
    @pytest.fixture(scope='module', autouse=True)
    #打开浏览器，输入网址
    def open_browser(self):
        self.driver = webdriver.Chrome(executable_path=
                                      'C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe')
        # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
        self.driver.implicitly_wait(30)
        self.base_url = "http://81.70.24.116"
        self.driver.get(self.base_url + "/orangehrm/symfony/web/index.php/auth/login")
        yield
        self.driver.quit()
    #登陆页面
    @pytest.fixture(scope='module', autouse=True)
    def login(self,open_browser):
        driver = self.driver
        # driver.find_element_by_id("frmLogin").click()
        # 点击用户名文本框并清除输入admin
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        # 在密码框下清除，输入密码
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("root1234")
        # 点击登陆按钮
        driver.find_element_by_id("btnLogin").click()
    #添加员工
    @pytest.fixture(scope='module', autouse=True)
    def test_search(self,open_browser):
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_pim_addEmployee").click()
        driver.find_element_by_id("firstName").send_keys("李")
        driver.find_element_by_id("middleName").send_keys("世")
        driver.find_element_by_id("lastName").send_keys("民")
        driver.find_element_by_id("btnSave").click()


    def test_cart(self):
        pass

    @pytest.fixture(scope='module', autouse=True)
    def test_pay(self,open_browser):
        # 点击管理员工
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        # 点击工作
        self.driver.find_element_by_id("menu_admin_Job").click()
        # 点击职称
        self.driver.find_element_by_id("menu_admin_viewJobTitleList").click()
        # 点击添加
        self.driver.find_element_by_id("btnAdd").click()
        # 输入用户名
        self.driver.find_element_by_id("jobTitle_jobTitle").send_keys("唐太宗")
        # 点击保存
        self.driver.find_element_by_id("btnSave").click()
