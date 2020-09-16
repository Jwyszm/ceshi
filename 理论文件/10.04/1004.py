#-*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
# Author: lindafang
# Date: 2020-09-08 10:05
# File: test_selenium_hrmlogin.py

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class HrmLogin(unittest.TestCase):
    def setUp(self):
        # 通过驱动建立一个浏览器，
        self.driver = webdriver.Chrome(executable_path=
                                       '/Users/lindafang/PycharmProjects/seleniumautotest/driver/chromedriver')
        # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
        self.driver.implicitly_wait(30)
        self.base_url = "http://81.70.24.116"

    def test_hrm_login(self):
        driver = self.driver
        driver.get("/orangehrm/symfony/web/index.php/auth/login")
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
        # 是断言
        # self.assertEqual("欢迎admin", driver.find_element_by_id("welcome").text)
        assert "欢迎admin" == driver.find_element_by_id("welcome").text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()