#-*- coding:utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#定位页面

class LoginPageLocators(object):
    txtUsername=(By.ID,"txtUsername")
    txtPassword=(By.ID,"txtPassword")
    btnLogin=(By.ID,"btnLogin")

class WebcomePageLocators(object):
    welcome=(By.ID,"welcome")


class AdminUsePageLocators(object):
    menu_admin_viewAdminModule = (By.ID,"menu_admin_viewAdminModule")
    menu_admin_UserManagement = (By.ID,"menu_admin_UserManagement")
    menu_admin_viewSystemUsers = (By.ID,'menu_admin_viewSystemUsers')
    btnAdd=(By.ID,"btnAdd")
    systemUser_userType_select=(By.ID,'systemUser_userType')
    systemUser_employeeName_empName=(By.ID,'systemUser_employeeName_empName')
    systemUser_userName=(By.ID,'systemUser_userName')
    systemUser_status=(By.ID,'systemUser_status')
    systemUser_password=(By.ID,'systemUser_password')
    systemUser_confirmPassword=(By.ID,'systemUser_confirmPassword')
    btnSave=(By.ID,'btnSave')


class Pim_employpPageLocators(object):
    menu_pim_viewPimModule=(By.ID,'menu_pim_viewPimModule')
    menu_pim_viewEmployeeList=(By.ID,'menu_pim_viewEmployeeList')
    btnAdd=(By.ID,'btnAdd')
class zhicheng(object):
    menu_admin_viewAdminModule=(By.ID,'menu_admin_viewAdminModule')
    menu_admin_Job=(By.ID,'menu_admin_Job')
    menu_admin_viewJobTitleList=(By.ID,'menu_admin_viewJobTitleList')
    btnAdd=(By.ID,'btnAdd')
    jobTitle_jobTitle=(By.ID,'jobTitle_jobTitle')
    btnSave = (By.ID, 'btnSave')

