# -*-coding:utf-8-*-
from  testCase.login.testLogin import Login
import time,json
from testCase.base import Base

'''
其他入库单
'''

class OthersInto(Base):
    def __init__(self, cookie):
        self.page_url = '/storageios/new?category=in'
        super(OthersInto, self).__init__(cookie)

        self.body = {
            'number': 'QTRKD'+time.strftime("%Y%m%d%H%M%S"),
            'category': 'in',
            'storaged_at':time.strftime("%Y-%m-%d"),
            'total_quantity': '6.00',
            'total_base_quantity': '',
            'total_amount': '36.00',
            'note': '其他入库单接口自动化测试',
            'companyable_type': 'Customer',
            'companyable_id': '1465906',
            'check_id': '',
            'status': 'approving',
            'attachments_attributes[0][id]': '',
            'attachments_attributes[0][dn_key]': 'FmzjkW3DieyLz6dzs7byB0R9lDr0',
            'attachments_attributes[0][key]': 'FmzjkW3DieyLz6dzs7byB0R9lDr0',
            'attachments_attributes[0][filename]': 'lAHPBY0V40IDOmfM28zb_219_219.gif',
            'attachments_attributes[0][url]': 'https://obbsip92b.qnssl.com/FmzjkW3DieyLz6dzs7byB0R9lDr0?&e=1534999596&token=w2yRBQw0CPY-fsy6hxBjASopjHCTtT7RKFRtQeJz:yHHHwsz3uglkXtwOSAOcrbSF6k8=',
            'attachments_attributes[0][destroy]': 'false',
            'document_approvers_params[0][level]': '1',
            'document_approvers_params[0][member_ids][]': '1610270',
            'document_approvers_params[1][level]': '3',
            'document_approvers_params[1][member_ids][]': '1610270',
            'product_items_attributes[0][product_attr_group_id]': '3693590',
            'product_items_attributes[0][product_id]': '3254204',
            'product_items_attributes[0][product_unit_id]': '3505751',
            'product_items_attributes[0][warehouse_id]': '46311',
            'product_items_attributes[0][name]': '五月花',
            'product_items_attributes[0][product_number]': 'CP0001',
            'product_items_attributes[0][attr_names]': '',
            'product_items_attributes[0][spec]': '规格',
            'product_items_attributes[0][unit]': '包',
            'product_items_attributes[0][quantity]': '2.00',
            'product_items_attributes[0][base_unit]': '',
            'product_items_attributes[0][base_quantity]': '',
            'product_items_attributes[0][deputy_unit_quantity]': '',
            'product_items_attributes[0][price]': '5.00',
            'product_items_attributes[0][amount]': '10.00',
            'product_items_attributes[0][note]': '产品备注',
            'product_items_attributes[0][batch_number]': '',
            'product_items_attributes[0][produced_at]': '',
            'product_items_attributes[0][expired_at]': '',
            'product_items_attributes[0][modified]': 'quantity',
            'product_items_attributes[1][product_attr_group_id]': '3693598',
            'product_items_attributes[1][product_id]': '3254209',
            'product_items_attributes[1][product_unit_id]': '3505756',
            'product_items_attributes[1][warehouse_id]': '46311',
            'product_items_attributes[1][name]': 'iPhone8',
            'product_items_attributes[1][product_number]': 'CP0004',
            'product_items_attributes[1][attr_names]': '深空灰/64G',
            'product_items_attributes[1][spec]': 'iPhone的规格',
            'product_items_attributes[1][unit]': '部',
            'product_items_attributes[1][quantity]': '2.00',
            'product_items_attributes[1][base_unit]': '',
            'product_items_attributes[1][base_quantity]': '',
            'product_items_attributes[1][deputy_unit_quantity]': '',
            'product_items_attributes[1][price]': '6.00',
            'product_items_attributes[1][amount]': '12.00',
            'product_items_attributes[1][note]': 'iPhone的备注1',
            'product_items_attributes[1][batch_number]': '',
            'product_items_attributes[1][produced_at]': '',
            'product_items_attributes[1][expired_at]': '',
            'product_items_attributes[1][modified]': 'price',
            'product_items_attributes[2][product_attr_group_id]': '3693599',
            'product_items_attributes[2][product_id]': '3254209',
            'product_items_attributes[2][product_unit_id]': '3505756',
            'product_items_attributes[2][warehouse_id]': '46311',
            'product_items_attributes[2][name]': 'iPhone8',
            'product_items_attributes[2][product_number]': 'CP0004',
            'product_items_attributes[2][attr_names]': '玫瑰红/256G',
            'product_items_attributes[2][spec]': 'iPhone的规格',
            'product_items_attributes[2][unit]': '部',
            'product_items_attributes[2][quantity]': '2.00',
            'product_items_attributes[2][base_unit]': '',
            'product_items_attributes[2][base_quantity]': '',
            'product_items_attributes[2][deputy_unit_quantity]': '',
            'product_items_attributes[2][price]': '7.00',
            'product_items_attributes[2][amount]': '14.00',
            'product_items_attributes[2][note]': 'iPhone的备注2',
            'product_items_attributes[2][batch_number]': '',
            'product_items_attributes[2][produced_at]': '',
            'product_items_attributes[2][expired_at]': '',
            'product_items_attributes[2][modified]': 'price',
        }
        pass

    def new_category_others_in(self):

        headers = self.headers()
        headers = self.add_authorization_token(headers)
        # 新增其他入库单
        response = self.session.post(self.base_url + "/api/storageios.json", data=self.body,
                         headers=headers)
        j=json.loads(response.text)
        id=j["storageio"]["id"]
        print('其他入库单创建成功，id：',id)
        # 获取新增的其他入库单详情
        response = self.session.get(self.base_url + '/api/storageios/' + str(id) + '.json', headers=headers)
        response = json.loads(response.text)
        print('单据详情：',response)
        # 新增的其他入库单进行1级审批通过
        approving_json1 = {'status': 'approving','approved_level': '1','reason': '一级审批通过','resume_executing': False,'allow_negative_inventory': False,'gt_order_quantity': False}
        approving1 = self.session.put(self.base_url + '/api/storageios/'+str(id)+'.json', data=approving_json1,headers=headers)
        approving1 = json.loads(approving1.text)
        print('1级审批通过：',approving1)
        # 新增的其他入库单进行2级审批通过
        approving_json2 = {'status': 'approving','approved_level': '2','reason': '二级审批通过','resume_executing': False,'allow_negative_inventory': False,'gt_order_quantity': False}
        approving2 = self.session.put(self.base_url + '/api/storageios/'+str(id)+'.json', data=approving_json2,headers=headers)
        approving2 = json.loads(approving2.text)
        print('2级审批通过：',approving2)
        ## 新增的其他入库单进行3级审批通过
        approving_json3 = {'status': 'approving','approved_level': '3','reason': '三级审批通过','resume_executing': False,'allow_negative_inventory': False,'gt_order_quantity': False}
        approving3 = self.session.put(self.base_url + '/api/storageios/'+str(id)+'.json', data=approving_json3,headers=headers)
        approving3 = json.loads(approving3.text)
        print('3级审批通过：',approving3)

        #self.session.close()
        pass

    def custom_headers(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': self.base_url,
            'Connection': 'keep-alive',
        }
        return headers

if __name__ == '__main__':
    login = Login()
    login.user_login("13052371903", "111111")
    cookie = login.cookie
    othersinto = OthersInto(cookie)
    othersinto.new_category_others_in()

