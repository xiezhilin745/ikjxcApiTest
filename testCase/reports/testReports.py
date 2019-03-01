import unittest
'''
各种报表全都写在一个文件中
每个报表分别封装成对应报表的方法 
查看报表时需要走一遍创建报表中单据的流程 再去查报表list 看下新增的单据是否存在报表中
'''

class MyTestCase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        print('结束')

    @classmethod
    def setUpClass(cls):
        print('开始')

    def setUp(self):
        print('开始')

    def tearDown(self):
        print('结束')



    def test_something(self):
        print('1')

    def test_something2(self):
        print('2')
    def test_something3(self):
        print('3')


if __name__ == '__main__':
    unittest.main()
