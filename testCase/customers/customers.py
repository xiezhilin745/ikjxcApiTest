# -*-coding:utf-8-*-
from  testCase.login.testLogin import Login
from  commons.common import Commons
import requests
import time
from bs4 import BeautifulSoup
from testCase.base import Base

'''
各种增加客户的实现
'''

class AddCustomers(Base):
    def __init__(self, cookie):
        self.page_url = '/customers'
        super(AddCustomers, self).__init__(cookie)

        self.customer_name = '接口测试'+time.strftime("%Y-%m-%d-%H:%M:%S")
        self.customer_number = time.strftime("%Y-%m-%d-%H:%M:%S")
        self.customer_default_amount = '10'
        self.customer_address = '地址'
        self.customer_note = '备注'

        self.body = {
            "utf8": "✓",
            "type": "",
            "customer[name]": self.customer_name,
            "customer[number]": self.customer_number,
            "customer[default_amount]": self.customer_default_amount,
            "customer[address]": self.customer_address,
            "customer[note]": self.customer_note,
            'customer[customer_type_id]': '107690',
            'customer[assignee_id]': '1610266',
            'customer[assistor_ids][]': '1610265',
            'customer[text_field_3c9b7f728d]': '100',
            'customer[attachments][][key]': 'Fm2a6UUUUfjmXcCLZ1w5YCG1DzGe',
            'customer[attachments][][filename]': 'lADOpN5kps0B4M0B4A_480_480.jpg',
            'customer[attachments][][url]': 'https://obbsip92b.qnssl.com/Fm2a6UUUUfjmXcCLZ1w5YCG1DzGe?&e=1534777754&token=w2yRBQw0CPY-fsy6hxBjASopjHCTtT7RKFRtQeJz:yYiQUtSHZlQ2M1sRNwhkwC0qHac=',
            'customer[attachments][][_destroy]': 'false',
            'customer[contacts_attributes][0][name]': '谢师傅',
            'customer[contacts_attributes][0][mobile]': '13052371907',
            'customer[contacts_attributes][0][telephone]': '0755-827773816',
            'customer[contacts_attributes][0][email]': '123@qq.com',
            'customer[contacts_attributes][0][address]': '联系人地址',
            'customer[contacts_attributes][0][is_primary]': 'primary',
            'customer[contacts_attributes][0][note]': '联系人备注',
            'customer[contacts_attributes][0][_destroy]': 'false',
            'customer[contacts_attributes][0][org_id]': '21862'
        }

        self.param = {
            "page": "1",
            "per": "15",
            "assignee_id": "all",
            "department_id": "all",
            "customer_type_id": "",
            "keyword": self.customer_name,
            "keyword_type": "customers.name"
        }

        pass

    #添加普通客户
    def add_ordinary_customer(self):

        headers = self.headers()
        headers = self.add_authorization_token(headers)
        #新增客户
        response = self.session.post(url=self.current_url, data=self.body, headers=headers)
        print('客户Add状态码：',response.status_code)
        #查询新增的客户
        response = self.session.get(self.base_url + "/api/customers/query_by_custom_columns.json", params=self.param,
                             headers=headers)
        response = response.json()
        #获取返回的customers第1个客户名称
        response = response['customers'][0]['name']
        print('客户添加成功，客户名称：',response)
        #self.session.close()

def base_headers():
    pass


if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie

    customers = AddCustomers(cookie)
    customers.add_ordinary_customer()


    pass


