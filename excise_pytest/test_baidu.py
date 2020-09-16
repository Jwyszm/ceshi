#-*- coding:utf-8 -*-
import pytest,allure,time
from selenium import webdriver
@allure.description("测试百度搜索功能")
@allure.severity("critical")
@allure.story("正确的测试用例")
def test_add_caculation1():
    with allure.step("打开驱动"):
        driver = webdriver.Chrome(executable_path=
                                   'C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe')
    # 全局智能等待为30，出现错误，等待30秒，每5秒检查一次，如果30秒到了，还是错误报错。
    driver.implicitly_wait(30)
    with allure.step("打开网页"):
        driver.get("https://www.baidu.com/")
    with allure.step("点击输入"):
        driver.find_element_by_id("kw").send_keys("allure")
    time.sleep(2)
    with allure.step("点击搜索按钮"):
        driver.find_element_by_id("su").click()
    time.sleep(2)
    with allure.step('截图验证'):
        driver.save_screenshot("./result/c.png")
        allure.attach.file("./result/c.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("退出"):
        driver.quit()