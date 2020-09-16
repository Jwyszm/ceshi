#-*- coding:utf-8 -*-
import pytest,sys
# def setup_module():
#     print("这是一个文件在开始时执行一次")
# def teardown_module():
#     print("这是一个文件在结束时执行一次")
# def setup_function():
#     print("这个方法里的，在，不在类的方法的每个函数前执行一次")
# def test_function_01():
#     print("不在类中的方法01")
# def test_function_02():
#     print("不在类中的方法02")
# def teardown_function():
#     print("这个方法里的，在，不在类的方法的每个函数后执行一次")

class TestCalss():
    # def setup_class(self):
    #     print("类开始时执行一次")
    # def teardown_class(self):
    #     print("类结束时执行一次")
    #
    # def teardown_method(self):
    #     print("类中方法每个函数后执行一次")
    #
    # def setup_method(self):
    #     print("类中方法每个函数前执行一次")
    #
    # # 跳过的第一种方法
    # @pytest.skip
    # def test_function_01(self):
    #     print("在类中的方法01")
    #     assert 3==2+1
    #     assert (3>2)==True
    #     assert "linda" in "lindafang"
    #     assert ["1"]==[1]
    #
    # # 跳过的第二种方法
    # @pytest.mark.skip
    # def test_function_02(self):
    #     print("在类中的方法02")
    #     assert {'name':"linda","age":18}=={'name':"linda","age":38}
    #
    # # 跳过的第三种方法
    # @pytest.mark.skipif(reason="不想执行")
    # def test_function_03(self):
    #     print("在类中的方法03")
    #     assert '*' * 10 == "*" * 5
    def setUp(self):
        print('每个方法都执行一次')
    environment='android'
    @pytest.mark.skipif(environment=="android",reason='android平台没有这个功能')
    def test_cart_3(self):
        print("case3,登陆，点击苹果图标")
    @pytest.mark.skipif(sys.platform=='win32',reason="不在1")
    @pytest.mark.skipif(sys.version_info<(3,9),reason="不在2")
    def test_cart(self):
        print("case3,登陆点击图标，3.9版本无法运行")
if __name__ == '__main__':
    pytest.main()
