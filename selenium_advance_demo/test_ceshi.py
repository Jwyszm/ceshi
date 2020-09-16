#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest


driver=webdriver.Chrome(executable_path="C:\\Users\\dell\\Desktop\\ceshi\\driver\\chromedriver.exe")

driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/pim/viewPersonalDetails/empNumber/1")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element(By.ID,"txtPassword").send_keys("root1234")
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
assert '欢迎admin' in driver.page_source

menu_admin_viewAdminModule=driver.find_element_by_id("menu_pim_viewPimModule")
menu_admin_viewSystemUsers=driver.find_element_by_id('menu_pim_viewEmployeeList')
ActionChains(driver)\
    .move_to_element(menu_admin_viewAdminModule)\
    .click(menu_admin_viewSystemUsers).perform()

assert '欢迎admin' in driver.page_source
driver.find_element_by_id("btnAdd").click()
driver.find_element_by_id("firstName").send_keys("长")
driver.find_element_by_id("middleName").send_keys("员")
driver.find_element_by_id("lastName").send_keys("委")
driver.find_element_by_id("btnSave").click()