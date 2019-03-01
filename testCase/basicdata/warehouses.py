# -*-coding:utf-8-*-
import time
from testCase.login.testLogin import Login
from testCase.base import Base


class WareHouses(Base):
    def __init__(self, cookie):
        self.page_url = '/warehouses'
        super(WareHouses, self).__init__(cookie)
        self.ware_houses_id = ''

    def add_warehouses(self):
        #仓库的data
        warehouses_data = {
            'warehouse[id]': '',
            'warehouse[number]': 'CK' + time.strftime("%H:%M:%S"),
            'warehouse[name]': '接口测试仓' + time.strftime("%H:%M:%S"),
            'warehouse[address]': '湖南长沙橘子洲',
            'warehouse[contacter_id]': '1610270',
            'warehouse[telephone]': '13052371907',
            'warehouse[note]': '我是仓库的备注',
            'warehouse[assistable_member_ids][]': ['1610263','1610261','1610266'],
            'warehouse[viewable_member_ids][]': ['1610263','1610261','1610266','1610270'],
            'warehouse[entity_all_viewable]': False
        }

        headers = self.headers()
        headers = self.all_headers(headers)
        r2 = self.session.post(self.base_url + '/warehouses.json', data=warehouses_data, headers=headers)
        r2 = r2.json()
        name = r2['warehouse']['name']
        self.ware_houses_id = r2['warehouse']['id']
        print('新增仓库成功，名称：',name,'id：',self.ware_houses_id )


    def disable_warehouses(self,state,warehouses_id):
        headers = self.headers()
        headers = self.all_headers(headers)

        #如果self.ware_houses_id等于空，就执行参数里面的id
        #如果self.ware_houses_id有值，就执行self.ware_houses_id
        if self.ware_houses_id == '':
            id = warehouses_id
            if id == '':
                print('warehouses_id为空，无法执行禁用/启用，已默认为46312')
                #默认湖南仓库，46312
                id = '46312'
        else:
            id = self.ware_houses_id

        #如果state为enabled，就是启用仓库，否则就是禁用
        if state == 'disabled':
            data = {
                #禁用disabled
                'warehouse[status]': 'disabled'
            }
            disable = self.session.put(self.base_url + '/warehouses/' + str(id) + '.json', data=data, headers=headers)
            disable = disable.json()
            name = disable['warehouse']['name']
            code = disable['status']['code']
            if code == 200:
                print('禁用成功,仓库name：', name)
            else:
                print('禁用失败，code不是200')
        else:
            data = {
                #启用enabled
                'warehouse[status]': 'enabled'
            }
            disable = self.session.put(self.base_url + '/warehouses/' + str(id) + '.json', data=data, headers=headers)
            disable = disable.json()
            name = disable['warehouse']['name']
            code = disable['status']['code']
            if code == 200:
                print('启用成功,仓库name：', name)
            else:
                print('启用失败，code不是200')


    def get_warehouses(self):
        headers = self.headers()
        headers = self.all_headers(headers)
        param = {
            "page": "1",
            "per": "15"
        }
        #加载第一页仓库列表
        warehouses_list =  self.session.get(self.base_url + '/warehouses.json',params=param,headers=headers)
        warehouses_list = warehouses_list.json()
        names = [x['name'] for x in warehouses_list['warehouses']]
        print('第一页仓库数：',len(names),'，\n名称：',names,'\n总仓数：',warehouses_list['pagination']['total_count'])

        #加载get_contacters.json
        contacters = self.session.get(self.base_url + '/warehouses/get_contacters.json',headers=headers)
        contacters = contacters.json()
        names = [x['name'] for x in contacters['contacters']]
        code = contacters['status']['code']
        if code == 200:
            print('contacters接口返回成功：', names,'\n')
        else:
            print('contacters接口返回失败，code不是200','\n')


        #加载get_assistors.json?id=
        assistors = self.session.get(self.base_url + '/warehouses/get_assistors.json?id=',headers=headers)
        assistors = assistors.json()
        names = [x['name'] for x in assistors['assistors']]
        code = contacters['status']['code']
        if code == 200:
            print('assistors接口返回成功：', names,'\n')
        else:
            print('assistors接口返回失败，code不是200','\n')

        #加载get_viewable_members.json?id=
        members = self.session.get(self.base_url + '/warehouses/get_viewable_members.json?id=',headers=headers)
        members = members.json()
        names = [x['name'] for x in members['viewable_members']]
        code = contacters['status']['code']
        if code == 200:
            print('viewable_members接口返回成功：', names,'\n')
        else:
            print('viewable_members接口返回失败，code不是200','\n')
        pass

if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie
    warehouses = WareHouses(cookie)
    warehouses.add_warehouses()
    houses_id = '46330' #houses_id为需要禁用的仓库id
    warehouses.disable_warehouses('no_disabled',houses_id)
    warehouses.get_warehouses()
