# -*-coding:utf-8-*-
from  testCase.login.testLogin import Login
from  commons.common import Commons
import requests
import time
from bs4 import BeautifulSoup
from testCase.base import Base

'''
各种增加供应商的实现
'''

class AddSuppliers(Base):
    def __init__(self, cookie):
        self.page_url = '/suppliers'
        super(AddSuppliers, self).__init__(cookie)

        self.supplier_name = '接口测试'+time.strftime("%Y-%m-%d-%H:%M:%S")
        self.supplier_number = time.strftime("%Y-%m-%d-%H:%M:%S")
        self.supplier_default_amount = '5'
        self.supplier_address = '地址南京东路'
        self.supplier_note = '备注'

        self.body = {
            "utf8": "✓",
            "type": "",
            "supplier[name]": self.supplier_name,
            "supplier[number]": self.supplier_number,
            "supplier[default_amount]": self.supplier_default_amount,
            "supplier[address]": self.supplier_address,
            "supplier[note]": self.supplier_note,
            'supplier[supplier_type_id]': '43499',
            'supplier[assignee_id]': '1610263',
            'supplier[assistor_ids][]': '1610270',
            'supplier[text_field_e4e8492fd0]': '80',
            'supplier[attachments][][key]': 'FucsDun_tumBUfcQbTY6gHlgxvia',
            'supplier[attachments][][filename]': 'u=2572528570,3179480776&fm=58&w=121&h=140&img.JPG',
            'supplier[attachments][][url]': 'https://obbsip92b.qnssl.com/FucsDun_tumBUfcQbTY6gHlgxvia?&e=1535102114&token=w2yRBQw0CPY-fsy6hxBjASopjHCTtT7RKFRtQeJz:hjqvSTlD4VRlG6Gd7ueLEdwu_jw=',
            'supplier[attachments][][_destroy]': 'false',
            'supplier[contacts_attributes][0][org_id]': '21862',
            'supplier[contacts_attributes][0][_destroy]': 'false',
            'supplier[contacts_attributes][0][name]': '库克',
            'supplier[contacts_attributes][0][mobile]': '13052371907',
            'supplier[contacts_attributes][0][telephone]': '021-5555010',
            'supplier[contacts_attributes][0][email]': '123@icloud.com',
            'supplier[contacts_attributes][0][address]': '美国纽约',
            'supplier[contacts_attributes][0][is_primary]': 'primary',
            'supplier[contacts_attributes][0][note]': '董事',

        }

        self.param = {
            "page": "1",
            "per": "15",
            "assignee_id": "all",
            "department_id": "all",
            "supplier_type_id": "",
            "keyword": self.supplier_name,
            "keyword_type": "suppliers.name"

        }

        pass

    #添加普通供应商
    def add_ordinary_supplier(self):

        headers = self.headers()
        headers = self.add_authorization_token(headers)
        #新增供应商
        response = self.session.post(url=self.current_url, data=self.body, headers=headers)
        print('供应商Add状态码：',response.status_code)
        #查询新增的供应商
        response = self.session.get(self.base_url + "/api/suppliers/query_by_custom_columns.json", params=self.param,
                             headers=headers)
        response = response.json()
        #获取返回的customers第1个供应商名称
        response = response['suppliers'][0]['name']
        print('供应商添加成功，供应商名称：',response)
        #self.session.close()

def base_headers():
    pass


if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie

    suppliers = AddSuppliers(cookie)
    suppliers.add_ordinary_supplier()

    pass


