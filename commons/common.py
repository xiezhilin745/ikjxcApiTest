#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
from  testCase.login.testLogin import Login


class Commons:

    def __int__(self):
        self.s=''
        self.headers=''
        self.cookie=''
        self.uid=''
        self.token=''
        pass

    def common_login(self):
        # print('在common_headers_cookies中执行登录')
        login = Login()
        login.Login("17755667777", "111111")
        self.cookie = login.cookie
        return self.cookie

    def common_requests_login(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.200 Safari/537.36",
            "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "X-Requested-With": "XMLHttpRequest",
        }

        #用self.cookie接受登录后返回的cookie
        self.cookie=Commons().common_login()
        #保持请求之间的Cookies
        self.s = requests.session()
        #更新cookie
        self.s.cookies.update(self.cookie)
        self.uid = self.cookie['uid']
        self.token = self.cookie['token']
        pass


if __name__ == '__main__':
    Commons().common_login()
    pass