#-*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from .base_operate import BasePage
from .locattors import LoginPageLocators
from .locattors import WebcomePageLocators
from .locattors import AdminUsePageLocators
from selenium.webdriver.support.wait import  WebDriverWait



class AdminUsePage(BasePage):
    def enter_xt(self):
        #智能等待
        menu = self.driver.find_element(*AdminUsePageLocators.menu_admin_viewAdminModule)
        # menu = self.driver.find_element(By.ID,"menu_admin_viewAdminModule")

        menu1 = self.driver.find_element(*AdminUsePageLocators.menu_admin_UserManagement)
        users = self.driver.find_element(*AdminUsePageLocators.menu_admin_viewSystemUsers)
        ActionChains(self.driver).move_to_element(menu).move_to_element(menu1).click(users).perform()

    def enter_btnAdd(self):
        btnAdd = self.driver.find_element(*AdminUsePageLocators.btnAdd)
        btnAdd.click()
    def systemUser_userType_select(self,index):
        systemUser_userType_select=self.driver.find_element(*AdminUsePageLocators.systemUser_userType_select)
        Select(systemUser_userType_select).select_by_index(int(index))

    def enter_systemUser_employeeName_empName(self, yuangongxingming):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*AdminUsePageLocators.systemUser_employeeName_empName))
        systemUser_employeeName_empName = self.driver.find_element(*AdminUsePageLocators.systemUser_employeeName_empName)
        systemUser_employeeName_empName.click()
        systemUser_employeeName_empName.clear()
        systemUser_employeeName_empName.send_keys(yuangongxingming)

    def enter_systemUser_userName(self, yhm):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*AdminUsePageLocators.systemUser_userName))
        systemUser_userName = self.driver.find_element(*AdminUsePageLocators.systemUser_userName)
        systemUser_userName.click()
        systemUser_userName.clear()
        systemUser_userName.send_keys(yhm)

    def systemUser_status(self,index):
        systemUser_status = self.driver.find_element(*AdminUsePageLocators.systemUser_status)
        Select(systemUser_status).select_by_index(int(index))
    def systemUser_password(self, mima):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*AdminUsePageLocators.systemUser_password))
        systemUser_password = self.driver.find_element(*AdminUsePageLocators.systemUser_password)
        systemUser_password.click()
        systemUser_password.clear()
        systemUser_password.send_keys(mima)
    def systemUser_confirmPassword(self, yzmm):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*AdminUsePageLocators.systemUser_confirmPassword))
        systemUser_confirmPassword = self.driver.find_element(*AdminUsePageLocators.systemUser_confirmPassword)
        systemUser_confirmPassword.click()
        systemUser_confirmPassword.clear()
        systemUser_confirmPassword.send_keys(yzmm)
    def enter_btnSave(self):
        btnSave = self.driver.find_element(*AdminUsePageLocators.btnSave)
        btnSave.click()
    def login_sucess_result(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*WebcomePageLocators.welcome))
        return self.driver.find_element(*WebcomePageLocators.welcome).test
