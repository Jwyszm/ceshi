#-*- coding:utf-8 -*-
#公共方法
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def save_picture(self,file_path):
        self.driver.save_screenshot(file_path)
