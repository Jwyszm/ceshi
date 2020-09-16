#-*- coding:utf-8 -*-
import pytest,allure
#单元自动化测试脚本


@allure.feature("这是一个加法计算器，加数0和加数1相加功能")
def add_caculation(num1,num2):
    sum=num1+num2
    return sum


@allure.description("这是一个加法计算器，测试了加分各种有效情况结果是否正确")
@allure.severity("critical")
@allure.story("正确的测试用例")
@allure.issue("","曾经的bug")
@allure.testcase("http://daohang.qq.com/?fr=hmpage","这是加法测试用例")
@pytest.mark.parametrize('num1,num2,result',[[1,2,3],
                                            [3,12,15],
                                            [6,-2,4],
                                            [1.8,2,3.8],
                                           ],ids=["十以内","十以外","负数","小数"]
                       )
def test_add_caculation1(num1,num2,result):
    with allure.step("第一步：调用加法的方法"):
        sum=add_caculation(num1,num2)
    with allure.step("断言加法结果和预期结果是否一致"):
        assert sum==num1+num2
    print(sum)

@allure.description("这是一个加法计算器，测试了加分各种无效情况结果是否正确")
@allure.severity("normal")
@allure.story("无效的测试用例")
@allure.testcase("http://daohang.qq.com/?fr=hmpage","这是加法测试用例")
@pytest.mark.parametrize('num1,num2,result',[["1",2,3],
                                            [3,"@",15],
                                            [6,-9999,4],
                                            [1.8,2,3.8],
                                           ],ids=["字符串","特殊字符","超长数","小数"]
                       )
def test_add_caculator_error(num1,num2,result):
    with allure.step("如果错误截图"):
        allure.attach.file("1.png",
                           attachment_type=allure.attachment_type.PNG)
    with allure.step("html网页的漂亮"):
        allure.attach("<html><body>这是我们要测试的加法<script type='text/javascript'>alert('这是一个惊喜');</script></body></html>",
                      "这是个网页", allure.attachment_type.HTML)
    with allure.step("执行了"):
        sum=add_caculation(num1,num2)
        allure.attach("加数1+加数2=", f"{0}+{1}={2}")
        assert sum ==result