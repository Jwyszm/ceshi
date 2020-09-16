# -*- coding:utf-8 -*-

'''
1.寻找发http请求库`requests
2.调用接口
验证协议层，验证状态吗，验证功能层时间是否符合


3.验证接口是否正确


...'''
import requests
def get_listusers_text():
    url = 'https://reqres.in/api/users?page=2'

    rep = requests.get(url)
    assert 200 == rep.status_code#响应状态码
    assert 2==rep.json()['page']#测试返回值
    print(rep.url)#返回url
    print(rep.text)#返回的响应以文本显示
    print  (rep.cookies)  # 缓存
    print  (rep.content)#二进制
    print  ( rep.headers)#头信息
    print(rep.encoding)#编码


    assert 50>rep.elapsed.total_seconds()#测试响应时间
def post_createuser_text():
    url = 'https://reqres.in/api/users'
    data={
        "name": "lindafang",
        "job": "leader"
    }
    rep = requests.post(url,data=data)
    assert 201 == rep.status_code
    assert 'linda' in rep.json()['name']
    assert 50 > rep.elapsed.total_seconds()
def put_text():
    url = 'https://reqres.in/api/users/2'
    data = {
    "name": "linda",
    "job": "zion resident"
}
    rep = requests.put(url, data=data)
    print(rep.status_code)
    assert 200 == rep.status_code
    assert 'linda' in rep.json()['name']
    assert 50 > rep.elapsed.total_seconds()


def patch_text():
    url = 'https://reqres.in//api/users/2'
    data = {
    "name": "linda",
    "job": "zion resident"
}
    rep = requests.patch(url, data=data)
    assert 200 == rep.status_code
    assert 'linda' in rep.json()['name']
    assert 50 > rep.elapsed.total_seconds()

def del_text():
    url = 'https://reqres.in//api/users/2'

    rep = requests.delete(url)
    assert 201 == rep.status_code
    assert 50 > rep.elapsed.total_seconds()
def request_get_datadriven():
    url = "https://reqres.in/api/users?page=2"
    headers = {"Referer": "https://reqres.in/",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

    # 这是一个将所有请求方法封装后的统一写法。
    rep=requests.request(method='get',url=url,headers=headers)
    print(rep.json())

if __name__ == '__main__':
    get_listusers_text()


