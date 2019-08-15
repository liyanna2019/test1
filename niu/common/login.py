# -*- coding: utf-8 -*-
import requests
import re



class Login(object):
    def niu_login(self):
        url = "http://testdl.fxchat.cn/api/Login"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
        }
        s = requests.session()
        s.post("http://218.244.157.23:8090/", headers=headers)
        d ={
            "loginName": 18219111882,
            "password": 'a123456',
            "terminal": "5"
        }
        login = s.post(url, data=d, headers=headers)
        #userKey = login.json()['bodyMessage']['userKey']
        #print(userKey)
        result = login.json()
        return result




if __name__ == "__main__":
    Login().login()


