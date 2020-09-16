#-*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from .base_operate import BasePage
from .locattors import LoginPageLocators
from .locattors import WebcomePageLocators
from .locattors import zhicheng
from selenium.webdriver.support.wait import  WebDriverWait
class Job1(BasePage):
    def enter_xt(self):
        #智能等待
        menu  = self.driver.find_element(*zhicheng.menu_admin_viewAdminModule)
        menu1 = self.driver.find_element(*zhicheng.menu_admin_Job)
        users = self.driver.find_element(*zhicheng.menu_admin_viewJobTitleList)
        ActionChains(self.driver).move_to_element(menu).move_to_element(menu1).click(users).perform()
    def enter_btnAdd(self):
        btnAdd = self.driver.find_element(*zhicheng.btnAdd)
        btnAdd.click()
    def enter_btnSave(self):
        btnSave = self.driver.find_element(*zhicheng.btnSave)
        btnSave.click()
    def zc(self, zc):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*zhicheng.jobTitle_jobTitle))
        jobTitle_jobTitle = self.driver.find_element(*zhicheng.jobTitle_jobTitle)
        jobTitle_jobTitle.click()
        jobTitle_jobTitle.clear()
        jobTitle_jobTitle.send_keys(zc)