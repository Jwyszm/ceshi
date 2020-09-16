#-*- coding:utf-8 -*-
import requests
@classmethod
def access_token_T():
    url=' https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxf6d105886c9515a0&secret=84c045a0fbf89c453e2ec025edc854d0'
    rep=requests.get(url)
    cls.access_tokeb= rep.json()['access_token']

def test_access_token_T():
    url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token='+self.access_token_T()
    data={
        "tag": {"name": "linda" }
    }
    rep=requests.post(url=url,json=data)
    print(rep.json())
#     print(rep.text)
#     assert 200==rep.status_code
#     rep_json=rep.json()
#     assert  7200 == rep_json['expires_in']
# def test_access_token_F():
#     pass
if __name__ == '__main__':
    test_access_token_T()