#-*- coding:utf-8 -*-
import pytest


# @pytest.fixture(params=[1,2,3,'linda'])
# def data_fixtrue_param(request):
#     return request.param
#
#
# def test_fixtrue_param(data_fixtrue_param):
#     print(data_fixtrue_param,type(data_fixtrue_param))

# @pytest.mark.parametrize('num12,result',[('1+2',3),
#                                             ('3+12',15),
#                                             ('6*2',13),
#                                             ('3/1',3),
#                                            ])
# def test_counlator(num12,result):
#     assert eval(num12)==result
# @pytest.mark.parametrize('num1,num2,result',[[1,2,3],
#                                             [3,12,15],
#                                             [6,-2,4],
#                                             [1.8,2,3.8],
#                                            ],ids=["十以内","十以外","负数","小数"]
#                          )
#
# def test_counlator2(num1,num2,result):
#     assert num1+num2 == result
#     print(result)

test_user=[{"name":"admin","password":"root1234"},
    {"name":'linda',"password":"root1234"},
    {"name":"gaoyongqiang","password":"root1234"},
    {"name":"duxincheng","password":"root1234"}]


@pytest.fixture(scope="module")
def login(request):
    username=request.param["name"]
    password=request.param["password"]

    print(f"\n打开开首页准备登陆,用户名：{username},密码：{password}")
    return request.param

@pytest.mark.parametrize("login",test_user,indirect=True,ids=["老师","同学","同学","同学"])
def test_login(login):
    name=login["name"]
    password = login["password"]
    print(f"本次登陆的是{name},密码：{password}")
    assert name!=''