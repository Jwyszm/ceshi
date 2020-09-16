#-*- coding:utf-8 -*-
from ddt import ddt,file_data
import unittest

@ddt
class Testddt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类前执行")


    @file_data("shuju.yaml")
    def testddtt(self,*value):
        print(value)




