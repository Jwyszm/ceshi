#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import *
from selenium import *
import time
import pytest
import unittest
from selenium.webdriver.support.select import Select

class TestHrmLoginAdduser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe")
        driver=cls.driver
        driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/pim/viewPersonalDetails/empNumber/1")
        driver.maximize_window()
        driver = cls.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element(By.ID, "txtPassword").send_keys("root1234")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.minimize_window()



    def test_adduser(self):
        menu_admin_viewAdminModule = self.driver.find_element_by_id("menu_admin_viewAdminModule")
        menu_admin_UserManagement = self.driver.find_element_by_id("menu_admin_UserManagement")
        menu_admin_viewSystemUsers = self.driver.find_element_by_id('menu_admin_viewSystemUsers')
        ActionChains(self.driver) \
            .move_to_element(menu_admin_viewAdminModule) \
            .move_to_element(menu_admin_UserManagement) \
            .click(menu_admin_viewSystemUsers).perform()
        time.sleep(2)
        self.driver.find_element_by_id("btnAdd").click()
        systemUser_userType=self.driver.find_element_by_id("systemUser_userType")
        Select(systemUser_userType).select_by_value("1")
        # # select(systemUser_userType).select_by_visible_test("管理员")
    #
    #
    #     # # select(systemUser_userType).select_by_index("0")
    #     self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("li 世 李")
    #     self.driver.find_element_by_id("systemUser_userName").send_keys("123400")
    #     systemUser_status = self.driver.find_element_by_id("systemUser_status")
    #     Select(systemUser_status).select_by_value("0")
    #     self.driver.find_element_by_id("systemUser_password").send_keys("12341234")
    #     self.driver.find_element_by_id("systemUser_confirmPassword").send_keys("12341234")
    #     self.driver.find_element_by_id("btnSave").click()
    #
    #     time.sleep(2)
    #
    # def test_job_adduser(self):
    #     menu_admin_viewAdminModule = self.driver.find_element_by_id("menu_admin_viewAdminModule")
    #     menu_admin_Job = self.driver.find_element_by_id("menu_admin_Job")
    #     menu_admin_viewJobTitleList = self.driver.find_element_by_id('menu_admin_viewJobTitleList')
    #     ActionChains(self.driver) \
    #         .move_to_element(menu_admin_viewAdminModule) \
    #         .move_to_element(menu_admin_Job) \
    #         .click(menu_admin_viewJobTitleList).perform()
    #     time.sleep(2)
    #     # 向上滚动
    #     self.driver.execute_script("window.scrollBy(0,300)")
    #     self.driver.find_element_by_id("ohrmList_chkSelectRecord_492").click()
    def test_pim_adduser(self):
        menu_pim_viewPimModule = self.driver.find_element_by_id("menu_pim_viewPimModule")
        menu_pim_viewEmployeeList = self.driver.find_element_by_id('menu_pim_viewEmployeeList')
        ActionChains(self.driver) \
            .move_to_element(menu_pim_viewPimModule) \
            .click(menu_pim_viewEmployeeList).perform()
        time.sleep(2)
        # 向上滚动
        self.driver.execute_script("window.scrollBy(0,300)")
        ohrmList_chkSelectRecord=self.driver.find_elements_by_name("chkSelectRow[]")
        # for i in ohrmList_chkSelectRecord:
        #     self.driver.find_element_by_id("ohrmList_chkSelectRecord_{}".format(i.get_attribute("value"))).click()
        ohrmList_chkSelectRecord[-1].click()





        # assert '欢迎admin' in self.driver.page_source
        # driver.find_element_by_id("btnAdd").click()
        # driver.find_element_by_id("firstName").send_keys("长")
        # driver.find_element_by_id("middleName").send_keys("员")
        # driver.find_element_by_id("lastName").send_keys("委")
        # driver.find_element_by_id("btnSave").click()


