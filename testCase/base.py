import requests
from bs4 import BeautifulSoup

class Base(object):
    def __init__(self, cookie):
        self.base_url = 'https://dingtalkjxc-staging.ikcrm.com'
        self.host = 'dingtalkjxc-staging.ikcrm.com'
        self.session = requests.session()
        self.session.cookies.update(cookie)
        self.uid = cookie['uid']
        self.token = cookie['token']
        self.current_url = self.base_url + self.page_url


    def base_headers(self):
        # 获取一次网页
        g = self.session.get(url=self.current_url)
        # 把网页传给BeautifulSoup
        soup = BeautifulSoup(g.text, "html.parser")
        # 根据BeautifulSoup解析的网页，获取name="csrf-token" content="xxxxx+xxx/x+x=="
        csrf = soup.find(attrs={"name": "csrf-token"})['content']
        headers = {
            "Host": self.host,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.200 Safari/537.36",
            "Accept": "*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRF-Token": csrf,
            "Referer": self.current_url
        }
        return headers

    #调用包含Authorization的headers
    def add_authorization_token(self, headers):
        return {
            **headers,
            **{ "Authorization": "Token token=" + self.token + ",uid=" + self.uid }
        }

    #自定义headers，默认为空
    def custom_headers(self):
        return {}

    #headers和自定义headers
    def headers(self):
        updated_headers = self.base_headers()
        updated_headers.update(self.custom_headers())
        return updated_headers

    def all_headers(self, headers):
        return {
            **headers,
            **{ "Authorization": "Token token=" + self.token + ",uid=" + self.uid,
                "Upgrade-Insecure-Requests": "1",
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': self.base_url,
                'Connection': 'keep-alive'
                }
        }

    #暂时没用到
    def requests_get(self, url, params, headers):
        self.session.get(url=url, params=params,headers=headers)


    def requests_post(self, url, params, headers):
        self.session.post(url=url, params=params, headers=headers)

