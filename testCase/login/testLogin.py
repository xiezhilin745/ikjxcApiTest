# -*- coding: utf-8 -*-
__author__ = 'Doris'
import json
from bs4 import BeautifulSoup
import requests,os

class Login:
    def __init__(self):
        #test登录地址
        # self.base_url=const.SIGN_IN_BASE_URL
        # self.csrf=''
        self.cookie=''
        self.username=''
        self.password=''
        self.response=''
        self.uid=''
        self.token=''
        self.base_login_url = 'https://dingtalkjxc-staging.ikcrm.com'
        pass

    '''
     登录实现方法：输入用户名和密码后调用获取token接口，取得tolen和uid ，在登录地址中拼接这两个参数
     login="http://dingtalkjxc-staging.ikcrm.com/dingtalk/sessions/new?authentication_token="+token+"&uid="+uid
    '''
      #这里获取的token是根据账户密码获得  唯一
    def get_token_and_uid(self, username, password):
        url = self.base_login_url+'/api/auth/get_token.json'
        r = requests.post(url, json={"login": username, "password": password})
    
        s = json.loads(r.text)
        self.uid = s["auth"]["uid"]
        self.token = s["auth"]["authentication_token"]
        pass

    #登录，用户名密码 ：17755667777   111111
    def login(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.200 Safari/537.36",
            "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
        }

        SIGN_IN_BASE_URL=self.base_login_url+'/dingtalk/sessions/new?authentication_token='
        login = SIGN_IN_BASE_URL + self.token + "&uid=" + self.uid
        r2 = requests.session()
        r2.get(login,headers=headers)
        print('登录成功')
        #c=r2.cookies.get_dict()
        #r2.cookies.update(c)
        self.cookie= r2.cookies.get_dict()
        #print(self.cookie)
        pass


    '''
    第二种登录方式
    '''
    def user_login(self, user, pwd):

        url_path =self.base_login_url +"/users/sign_in"
        g=requests.get(url_path)
        c = g.cookies.get_dict()
        cc = c['_ik_invoicing_session']
        soup = BeautifulSoup(g.text, "html.parser")
        csrftoken = soup.find(attrs={"name": "authenticity_token"})['value']
        body = {
            "utf8": "✓",
            "authenticity_token": csrftoken,
            "user[login]": user,
            "user[password]": pwd,
            "user[remember_me]": "0",
            "commit": "登 录"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.200 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "Connection": "keep-alive",
            "Host": "dingtalkjxc-staging.ikcrm.com",
            "Origin": self.base_login_url,
            "Referer": self.base_login_url+"/users/sign_in?show_all_version=1",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "max-age=0",
            "Cookie": "_ik_invoicing_session=" + cc
        }
        s = requests.session()
        # s.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        # s.verify = os.getcwd()+'/charles-proxy-ssl-proxying-certificate.pem'
        s.post(self.base_login_url+"/users/sign_in", data=body, headers=headers)
        self.cookie=s.cookies.get_dict()
        self.uid = self.cookie['uid']
        self.token = self.cookie['token']
        print(self.base_login_url+'/dingtalk/sessions/new?authentication_token='+self.token+'&uid='+self.uid)
        s.close()
        pass


if __name__ == '__main__':
    #超管：13052371902，普通：13052371903
    login=Login()
    login.user_login("13052371903", "111111")
    #login.get_token_and_uid("17755667777", "111111")
    #login.login()
    #print(login.cookie)






