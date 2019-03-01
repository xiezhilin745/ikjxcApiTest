#-*-coding:utf-8-*-
import requests
import json,sys,io,os

class LxLogin:
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    def __init__(self):
        self.mobile_url ='https://lixiaojxc-staging.ikcrm.com'
        self.token =''
        self.uid = ''
        self.cookie=''

    def mobile_login_json(self,username,password):
        response = requests.post(url=self.mobile_url+'/api/auth/get_token.json',json={"login": username, "password": password})
        j=json.loads(response.text)
        self.token=j['auth']['authentication_token']
        self.uid=j['auth']['uid']
        s = requests.session()
        responses = s.get(self.mobile_url+'/mobile/dashboard?authentication_token='+self.token+'&uid='+self.uid)
        print('首页状态码：',responses.status_code)
        self.cookie=responses.cookies.get_dict()

    def pc__login_json(self,username,password):
        response = requests.post(url=self.mobile_url+'/api/auth/get_token.json',json={"login": username, "password": password})
        j=json.loads(response.text)
        self.token=j['auth']['authentication_token']
        self.uid=j['auth']['uid']
        s = requests.session()
        s.proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        s.verify = os.getcwd()+'/charles-proxy-ssl-proxying-certificate.pem'
        s.get(self.mobile_url+'/dingtalk/sessions/new?authentication_token='+self.token+'&uid='+self.uid)
        self.cookie=s.cookies.get_dict()
        # self.uid = self.cookie['uid']
        # self.token = self.cookie['token']
        print(self.mobile_url+'/dingtalk/sessions/new?authentication_token='+self.token+'&uid='+self.uid)
        pass


if __name__ == '__main__':
    login = LxLogin()
    #login.mobile_login_json('13555555555','111111')
    login.pc__login_json('13377777777','111111')
    print(login.cookie)
