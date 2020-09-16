# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random

#四种操作方法方式搜索定位

#i打开浏览器
driver=webdriver.Chrome("C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe")
#2输入地址
driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/pim/viewMemberships/empNumber/1")
#3输入用户名，找到用户名所在文本框，定位方式：id，name,css
#按照id名称进行搜素定位
driver.find_element_by_id("txtUsername").send_keys("admin")
#xpath按照位置进行搜素定位
driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("admin")
#按照name名称搜素定位
driver.find_element_by_name("txtUsername").send_keys("admin")
#按照class类名进行搜索定位
driver.find_element_by_css_selector("form-hint").send_keys("admin")


#输入密码
driver.find_element_by_id("txtPassword").send_keys("root1234")
#点击确认按钮
driver.find_element_by_id("btnLogin").click()
#点击管理员
driver.find_element_by_id("menu_admin_viewAdminModule").click()
#点击工作
driver.find_element_by_id("menu_admin_Job").click()
#点击职称
driver.find_element_by_id("menu_admin_viewJobTitleList").click()
#点击添加
driver.find_element_by_id("btnAdd").click()
#设计随机数
a=random.randint(1,10)
#输入用户名
driver.find_element_by_id("jobTitle_jobTitle").send_keys("admin"+str(a))
#点击保存
driver.find_element_by_id("btnSave").click()
#关闭当前窗口
driver.close()
#关闭所有页
driver.close.quit()
