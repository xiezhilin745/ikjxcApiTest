# -*-coding:utf-8-*-
from  testCase.login.testLogin import Login
from  commons.common import Commons
import requests
import json
from bs4 import BeautifulSoup
from testCase.base import Base

'''
各种查看供应商的实现
'''


class GetSuppliers(Base):
    def __init__(self, cookie):
        self.page_url = '/suppliers'
        super(GetSuppliers, self).__init__(cookie)

        self.param = {
            "page": "1",
            "per": "15",
            "assignee_id": "all",
            "department_id": "all",
            "supplier_type_id": "",
            "keyword": "",
            "keyword_type": "suppliers.name"
        }

    # 获取供应商列表
    def get_supplier_list(self):
        headers = self.headers()
        headers = self.add_authorization_token(headers)

        # 在地址后面拼接的参数，需要params传递
        response = self.session.get(self.base_url + "/api/suppliers/query_by_custom_columns.json", params=self.param,
                             headers=headers)
        response = response.json()
        names = [x['name'] for x in response['suppliers']]
        print('获取第一页供应商数',len(names),'，名称：\n',names,'\n总数：',response['pagination']['total_count'])
        #print('获取第1页供应商列表：\n',json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2))
        #self.session.close()
        pass


if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie
    suppliers = GetSuppliers(cookie)
    suppliers.get_supplier_list()

    print('获取供应商')
