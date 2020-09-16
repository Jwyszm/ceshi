#-*- coding:utf-8 -*-
import pytest
import allure



if __name__ == '__main__':
    # pytest.main(['-s','test_pytest_allure.py'])
    pytest.main(['-s','test_pytest_allure.py','--allure-stories','正确的测试用例'])
    pytest.main(['-s','test_pytest_allure.py','--allure-features','加法的计算器测试'])
    # pytest -s test_pytest_allure.py
    # pytest -s test_pytest_allure.py --allure-features="加法的计算器测试"
    # pytest -s test_pytest_allure.py --allure-stories="正确的测试用例"