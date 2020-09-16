#-*- coding:utf-8 -*-
# Author: lindafang
# Date: 2020-09-08 10:05
# File: test_selenium_hrmlogin.py


#这事ddt框架应用下的人力添加操作，之后可以自动生成截图，完全成功，
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re,os
from HTMLTestRunner import HTMLTestRunner


#-*- coding:utf-8 -*-
#"第一步进行导包"
#在类似加上ddt
#在需要数据测试的方法上file_data文件上传


from ddt import ddt,file_data

@ddt
class HrmLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 通过驱动建立一个浏览器，
        cls.driver = webdriver.Chrome(executable_path=
                                       'C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe')
        # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://81.70.24.116"


    def test_1hrm_login(self):
        driver = self.driver
        driver.get(self.base_url+"/orangehrm/symfony/web/index.php/auth/login")
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
        # 点击管理员
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        # 点击工作
        self.driver.find_element_by_id("menu_admin_Job").click()
        # 点击职称
        self.driver.find_element_by_id("menu_admin_viewJobTitleList").click()
        assert "欢迎admin" in driver.page_source

    @file_data("login1.yaml")
    def test_hrm_job(self, **value):
        print(value)
        username = value.get('username')

        # 点击添加
        self.driver.find_element_by_id("btnAdd").click()
        # 输入用户名
        self.driver.find_element_by_id("jobTitle_jobTitle").send_keys(username)
        # 点击保存
        self.driver.find_element_by_id("btnSave").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.save_screenshot("0.png")
        cls.driver.quit()
        # 9截屏

if __name__ == "__main__":
    # unittest.main()
    #提加报告
    # Suite套件,提交多个测试用例
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # 添加报告
    # suite套件，由多个测试用例组成。
    suite=unittest.TestSuite()
    # 通过类名把要测试类及类中方法加载到套件中
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HrmLogin))
    # 执行用例--执行结果保存到html格式报告。
    with open("result.html",'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title="测试报告",
            description="UI测试"
        )
        runner.run(suite)