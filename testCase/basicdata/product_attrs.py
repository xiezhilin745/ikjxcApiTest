# -*-coding:utf-8-*-
import time
from testCase.login.testLogin import Login
from testCase.base import Base

class ProductAttrs(Base):
    def __init__(self, cookie):
        self.page_url = '/product_attrs'
        super(ProductAttrs, self).__init__(cookie)
        self.id = ''
        self.name = ''
        self.headers = self.headers()
        self.headers = self.all_headers(self.headers)


    def get_attrs(self):
        '''
        获取属性分类的属性列表
        '''
        r2 = self.session.get(self.base_url + '/api/product_attrs.json?page=1&per=15&category=attributed&parent_id=90556', headers=self.headers)
        r2 = r2.json()
        print('获取“颜色”分类的属性列表：',r2['status'])


    def add_attrs(self):
        '''
        新增属性分类
        '''
        #新增重名的属性
        r2 = self.session.post(self.base_url + '/api/product_attrs.json', data={ 'name': '颜色', 'category': 'classified', 'parent_id': '' }, headers=self.headers)
        r2 = r2.json()
        message = r2['status']['message']
        print('测试新增重名属性分类：',r2)

        #属性分类的data
        attrs_data = {
            'name': '属性分类'+time.strftime("%m-%d-%H:%M:%S"),
            'category': 'classified',
            'parent_id': ''
        }
        r = self.session.post(self.base_url + '/api/product_attrs.json', data=attrs_data, headers=self.headers)
        r = r.json()
        #print(r)
        self.id = r['product_attr']['id']
        self.name = r['product_attr']['name']
        print('成功新增：',self.name,'分类')

    def add_attr(self):
        '''
        新增属性值
        '''
        # 为self.id分类新增属性值
        attr_data = {
            'name': '属性值' + time.strftime("%m-%d-%H:%M:%S"),
            'category': 'attributed',
            'parent_id': str(self.id)
        }

        r = self.session.post(self.base_url + '/api/product_attrs.json', data=attr_data, headers=self.headers)
        r = r.json()
        name = r['product_attr']['name']
        print('成功为【',self.name,'】分类新增【', name, '】值')

        #为【接口测试专用】分类新增属性值
        attr_data2 = {
            'name': '属性值' + time.strftime("%m-%d-%H:%M:%S"),
            'category': 'attributed',
            'parent_id': '90604'
        }
        r2 = self.session.post(self.base_url + '/api/product_attrs.json', data=attr_data2, headers=self.headers)
        r2 = r2.json()
        name2 = r2['product_attr']['name']
        print('成功为【 接口测试专用 】分类新增【', name2, '】值')



    def del_attrs(self,attrs_id):
        '''
        删除属性分类
        '''
        if self.id == '':
            id = attrs_id
            if id == '':
                print('attrs_id为空，已默认为90556【颜色】分类，无法删除')
                #默认湖南仓库，46312
                id = '90556'
            else:
                print('id不存在，无法删除...')
        else:
            id = self.id

        #删除add_attrs方法里面新增的属性分类
        r2 = self.session.delete(self.base_url + '/api/product_attrs/'+str(id)+'.json', headers=self.headers)
        print('成功删除：',self.name,'分类')

        #测试删除被产品占用的属性分类
        r1 = self.session.delete(self.base_url + '/api/product_attrs/90556.json', headers=self.headers)
        r1 = r1.json()
        print('测试无法删除的属性分类：',r1)


if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie
    attrs = ProductAttrs(cookie)
    attrs.get_attrs()
    attrs.add_attrs()
    attrs.add_attr()
    attrs.del_attrs('默认删除self.id')