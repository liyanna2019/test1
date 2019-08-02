# -*- coding: utf-8 -*-
import requests
import re

#构造request headers
url = "http://testdl.fxchat.cn/api/Login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
s = requests.session()

#构造登录函数
def login(name,password):
    s.post("http://218.244.157.23:8090/",headers=headers)
    d ={
        "loginName": name,
        "password": password,
        "terminal": "5"
    }
    login = s.post(url, data=d, headers=headers)
    print(login.content)
    #code = re.findall(r'"code ":"(.*?)"', login.content)
    #print('code=', code)


if __name__ == '__main__':
    name = input('请输入你的 用户名\n>  ')
    password = input("请输入你的密码\n>  ")
    login(name, password)

