#-*-coding:utf-8-*-
import unittest
from  testCase.customers.customers import AddCustomers
from  testCase.suppliers.suppliers import AddSuppliers
from  testCase.customers.getcustomers import GetCustomers
from  testCase.wareHouseManagement.OthersIntoWarehouse import OthersInto
from  testCase.login.testLogin import Login
from  testCase.products.AddProducts import NewProduct
from  testCase.basicdata.warehouses import WareHouses

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        print('开始测试')
        login = Login()
        login.user_login("13052371903", "111111")
        cls.cookie=login.cookie
        pass


    def test_customer(self):
        # 新增客户
        customers = AddCustomers(self.cookie)
        customers.add_ordinary_customer()

        #获取客户列表
        getcustomers = GetCustomers(self.cookie)
        getcustomers.get_customer_list()

    def test_supplier(self):
        # 新增供应商
        supplier = AddSuppliers(self.cookie)
        supplier.add_ordinary_supplier()
        pass

    def test_newproduct(self):
        # 新增产品
        newpro = NewProduct(self.cookie)
        newpro.add_product(newpro.ordinary_data)
        pass

    def test_othersinto(self):
        # 新增其他入库单
        othersinto = OthersInto(self.cookie)
        othersinto.new_category_others_in()
        pass

    def test_warehouses(self):
        # 新增仓库
        warehouses = WareHouses(self.cookie)
        warehouses.add_warehouses()
        warehouses.disable_warehouses('disabled', '仓库id')
        warehouses.get_warehouses()
        pass


    @classmethod
    def tearDownClass(cls):
        print('所有测试用例执行完毕')

        pass

if __name__ == '__main__':
    print('开始')
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_customer"))
    suite.addTest(MyTestCase("test_newproduct"))
    suite.addTest(MyTestCase("test_othersinto"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


