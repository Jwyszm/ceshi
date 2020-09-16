#-*- coding:utf-8 -*-
from .base_operate import BasePage
from .locattors import LoginPageLocators
from .locattors import WebcomePageLocators
from selenium.webdriver.support.wait import  WebDriverWait



class LoginPage(BasePage):
    def enter_username(self,username):
        #智能等待
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.txtUsername))
        usernameele=self.driver.find_element(*LoginPageLocators.txtUsername)
        usernameele.click()
        usernameele.clear()
        usernameele.send_keys(username)
    def enter_password(self,Password):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*LoginPageLocators.txtPassword))
        txtPassword = self.driver.find_element(*LoginPageLocators.txtPassword)
        txtPassword.click()
        txtPassword.clear()
        txtPassword.send_keys(Password)
    def enter_btnlogin(self):
        btnLogin = self.driver.find_element(*LoginPageLocators.btnLogin)
        btnLogin.click()



    def login_sucess_result(self):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*WebcomePageLocators.welcome))
        return self.driver.find_element(*WebcomePageLocators.welcome).test
