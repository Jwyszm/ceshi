#-*- coding:utf-8 -*-
# Author: lindafang
# Date: 2020-08-31 10:33
# File: datadriventest.py
'''
达到的效果 ：将代码与数据分开，动静分开
数据驱动框架：使用多个数据，循环执行某些代码，每次循环取一个数据执行。
如果实现：
使用第三方库ddt
1、pip install ddt
pip install Pyyaml
2、导入到代码中 from ddt import ddt
3、在类上面加@ddt
4、在使用数据驱动测试方法上面加@data
unpack是拆包，把列表去掉
5、在括号使用参数传递数据
'''
from ddt import ddt,data,unpack,file_data
import unittest

@ddt
class TestDataDriven(unittest.TestCase):
    @unittest.skip
    @data(1,2,3)
    def test_string(self,testcase):
        print("这是测试用例:"+str(testcase))

    @unittest.skip
    @data([1],['linda'],['汉字'])
    @unpack
    def test_list_unpack(self,datacase):
        print("这是列表测试用例:" + str(datacase))

    @unittest.skip
    @data([1,2],[3,4])
    @unpack
    def test_list(self,value1,value2):
        print(value1,value2)
        assert value1+1==value2
    @unittest.skip
    @data(('name','linda'),('linda','beautiful'),('female','1'))
    @unpack
    def test_tuple(self,data1,data2):
        print(data1,data2)
    @unittest.skip
    @data({'name':'linda'},{'name':'gaoyongqiang'})
    def test_dict(self,value3):
        print(value3)
    @unittest.skip
    @data({'name': 'linda'}, {'name': 'gaoyongqiang'})
    @unpack
    def test_dict1(self, name):
        print(name)



if __name__ == '__main__':
    unittest.main()
