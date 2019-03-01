# -*-coding:utf-8-*-
import requests,json,time
from testh5.login.LixiaoLogin import LxLogin


class OthersIntoWaerhouse:
    def __init__(self):
        self.mobile_url = 'http://lixiaojxc-staging.ikcrm.com'

    def new_others_in(self, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 wxwork/2.4.20 MicroMessenger/6.3.22 Language/zh',
            'Authorization': 'Token token=' + login.token + ', uid=' + login.uid,
            'Accept-Language': 'zh-cn',
            'Origin': self.mobile_url,
            'Content-Type': 'application/json'
        }
        headers2 = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 wxwork/2.4.20 MicroMessenger/6.3.22 Language/zh',
            'Authorization': 'Token token=' + login.token + ', uid=' + login.uid,
            'Accept-Language': 'zh-cn',
            'Origin': self.mobile_url,
            'Content-Type': 'application/json',
            'x-http-method-override':'PUT'
        }

        new_jsons = {
            "storageio": {"check_id": None, "companyable_name": "", "companyable_id": "", "companyable_type_name": "无",
                          "companyable_type": "", "warehouse_name": "", "warehouse_id": "",
                          "storaged_at": time.strftime("%Y-%m-%d"), "number": "QTRKD"+time.strftime("%Y%m%d%H%M%S"), "category": "in",
                          "document_category": "in", "category_i18n": "其他入库单", "product_items_attributes": [
                    {"modified": "price", "order_item_id": "", "product_unit_id": 4078, "name": "iPhone X",
                     "number": "CP0033", "product_number": "CP0033",
                     "image": "/assets/mobile/none-c3275f6a349d0b4ffcc94041eb841be7b758a2052971998d1b141a5ede0a08e0.png",
                     "attr_names": None, "spec": "", "unit": "瓶", "quantity": "1.000000", "price": "5.000000",
                     "price_with_tax": "0.000000", "discount": "0.000000", "deduction": "0.000000",
                     "amount": "5.000000", "amount_with_tax": "0.000000", "tax_amount": "0.000000",
                     "tax_rate": "0.000000", "note": "产品备注", "product_id": 3640, "product_attr_group_id": 4570,
                     "parent_id": "", "warehouse_id": 1, "warehouse_name": "浦东仓库", "batch_number": "", "batch_id": "",
                     "expired_at": "", "produced_at": "", "serial_codes_attributes": None,
                     "planned_production_quantity": "0.000000"}], "total_amount": 5, "total_quantity": 1,
                          "status": "approving", "note": "道路备注", "attachments": [], "removedAttachments": [],
                          "committing": True, "selecting_approvers": True, "namespace": "storageios_form",
                          "isConfig": True, "attachments_attributes": [],
                          "document_approvers_params": [{"level": "1", "member_ids": [21]},
                                                        {"level": "2", "member_ids": [21]}],
                          "document_addition_attributes": {"id": "", "copy_to": []},
                          "allow_negative_inventory": False}}

        # data = json.dumps(jsons)
        # post(data=data)
        s = requests.session()
        s.cookies.update(cookie)
        #新增其他入库单
        resp = s.post(self.mobile_url + '/api/storageios.json', json=new_jsons, headers=headers)
        j = json.loads(resp.text)
        id = j["storageio"]["id"]
        print('其他入库单新增成功：id：', id)
        # 获取新增的其他入库单详情
        response = s.get(self.mobile_url + '/api/storageios/' + str(id) + '.json', headers=headers)
        response = json.loads(response.text)
        print(response)
        #新增的其他入库单进行1级审批通过
        approval_json1 = {"storageio":{"status":"approving","approved_level":1,"reason":"一级通过","allow_negative_inventory":False},"_method":"PUT"}
        approval1 = s.post(self.mobile_url + '/api/storageios/' + str(id) + '.json', json=approval_json1,headers=headers2)
        approval1 = json.loads(approval1.text)
        print(approval1)
        # 新增的其他入库单进行2级审批通过
        approval_json2 = {"storageio":{"status":"approving","approved_level":2,"reason":"2级审批通过","allow_negative_inventory":False},"_method":"PUT"}
        approval2 = s.post(self.mobile_url + '/api/storageios/' + str(id) + '.json', json=approval_json2,headers=headers2)
        approval2 = json.loads(approval2.text)
        print(approval2)



if __name__ == '__main__':
    login = LxLogin()
    login.mobile_login_json('13052371907', '111111')
    oiw = OthersIntoWaerhouse()
    oiw.new_others_in(login.cookie)
