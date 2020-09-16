# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random
import datetime,time

#浏览器操作代码指令

#i打开浏览器
driver=webdriver.Chrome("C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe")
#窗口最大化
driver.maximize_window()
#2输入地址
driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/pim/viewMemberships/empNumber/1")
#按照id名称进行搜素定位
driver.find_element_by_id("txtUsername").send_keys("admin")
#输入密码
driver.find_element_by_id("txtPassword").send_keys("root1234")
#点击确认按钮
driver.find_element_by_id("btnLogin").click()
#刷新
driver.refresh()
#后退
driver.back()
#前进网页
driver.forward()

assert "欢迎admin" in driver.page_source
#9截屏
filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
driver.save_screenshot(filename+".png")
#全部退出
