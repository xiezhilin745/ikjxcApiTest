# -*-coding:utf-8-*-
from  testh5.login.LixiaoLogin import LxLogin
import requests,time,json
from bs4 import BeautifulSoup

'''
各种增加客户的实现
'''

class AddCustomers:
    def __init__(self):
        self.baser_url = 'https://lixiaojxc-staging.ikcrm.com'
        self.customer_url = self.baser_url+'/customers'

        self.customer_name = '接口测试'+time.strftime("%Y-%m-%d-%H:%M:%S")
        self.customer_number = time.strftime("%Y-%m-%d-%H:%M:%S")
        self.customer_default_amount = '10'
        self.customer_address = '美国洛杉矶'
        self.customer_note = '备注'
        self.body = {
            'utf8': '✓',
            'type': '',
            'customer[name]': self.customer_name,
            'customer[number]': self.customer_number,
            'customer[customer_type_id]': '468',
            'customer[default_amount]': self.customer_default_amount,
            'customer[address]': self.customer_address,
            'customer[assignee_id]': '634',
            "customer[note]": self.customer_note,
            'customer[assistor_ids][]': '275374',
            'customer[default_percentage]': '99',
            'customer[text_field_19ccf404df]': '客户文本内容',
            'customer[contacts_attributes][0][name]': '康师傅',
            'customer[contacts_attributes][0][mobile]': '13052371907',
            'customer[contacts_attributes][0][telephone]': '021-55556666',
            'customer[contacts_attributes][0][email]': '123@qq.com',
            'customer[contacts_attributes][0][address]': 'www.lixiaojxc.com',
            'customer[contacts_attributes][0][is_primary]': 'primary',
            'customer[contacts_attributes][0][note]': '康师傅有备注',
            'customer[contacts_attributes][0][_destroy]': 'false',
            'customer[contacts_attributes][0][org_id]': '89'
        }

        self.headers = {
            'Host': 'lixiaojxc-staging.ikcrm.com',
            'Connection': 'keep-alive',
            'Content-Length': '941',
            'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
            'Origin': self.baser_url,
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        pass

    #添加普通客户
    def add_ordinary_customer(self,cookie):
        s = requests.session()
        s.cookies.update(cookie)
        #获取一次网页
        g = s.get(url=self.customer_url)
        #把网页传给BeautifulSoup
        soup = BeautifulSoup(g.text, "html.parser")
        #根据BeautifulSoup解析的网页，获取name="csrf-token" content="Xxxxxxxxxx=="
        csrf = soup.find(attrs={"name": "csrf-token"})['content']

        headers = self.headers
        headers['Referer']=self.customer_url
        headers['X-CSRF-Token'] = csrf
        response = s.post(url=self.customer_url, data=self.body, headers=headers)
        print('客户Add状态码：',response.status_code)

    def get_customer(self,cookie):
        s = requests.session()
        s.cookies.update(cookie)
        uid = cookie['uid']
        token = cookie['token']

        #获取一次网页
        g = s.get(url=self.customer_url)
        #把网页传给BeautifulSoup
        soup = BeautifulSoup(g.text, "html.parser")
        #根据BeautifulSoup解析的网页，获取name="csrf-token" content="Xxxxxxxxxx=="
        csrf = soup.find(attrs={"name": "csrf-token"})['content']

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'lixiaojxc-staging.ikcrm.com',
            'Connection': 'keep-alive'
        }
        headers['Referer']=self.customer_url
        headers['X-CSRF-Token'] = csrf
        headers["Authorization"] = "Token token=" + token + ",uid=" + uid

        data = {
            'page': '1',
            'per': '15',
            'assignee_id': 'all',
            'department_id': 'all',
            'customer_type_id': '',
            'keyword': '',
            'keyword_type': 'customers.name'
        }
        # 在地址后面拼接的参数，需要params传递
        g = s.get('https://lixiaojxc-staging.ikcrm.com/api/customers/query_by_custom_columns',params=data,headers=headers)

        id = json.loads(g.text)
        ids = [ids['id'] for ids in id['customers']]
        print(ids)
        id2 = id['customers']
        print(id2)

        # response = g.json()
        # print(response)
        #print('客户GET结果：\n',json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2))




if __name__ == '__main__':
    lx = LxLogin()
    lx.pc__login_json('13377777777','111111')
    customers = AddCustomers()
    #customers.add_ordinary_customer(lx.cookie)
    customers.get_customer(lx.cookie)


