#-*- coding:utf-8 -*-
import requests
def get_listusers_test():
    url='https://reqres.in/api/users'

    rep=requests.get(url,params={'page':2})
    print(rep.headers)
    print(rep.json())




if __name__ == '__main__':
    get_listusers_test()