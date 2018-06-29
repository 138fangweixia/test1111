#coding:utf-8
import ddt
import unittest
from case.login import login
from common.readexcel import ExcelUtil
# 参数和代码分离
# testdata = [
#         {"username": "yunying1@jingdaka.com", "psw": "admin123"},
#         {"username": "yifan@jingdaka.com", "psw": "yifan123"},
#         {"username": "salemanager@jingdaka.com", "psw": "admin123"},
#         {"username": "kangyong@jingdaka.com", "psw": "kangyong"},
#          ]

readexcel = ExcelUtil("testdata.xlsx")
d11=readexcel.dict_data()
print(d11)

@ddt.ddt
class Test_login(unittest.TestCase):

    u''' crm系统登录模块'''
    def setUp(self):
        self.host="https://crm-test.jingdaka.com/api/crm"

    @ddt.data(*d11)
    def test_01(self,canshu):
        u''' 运营主管正确帐号密码登录'''
        print(canshu)
        self.username=canshu["username"]
        self.password=canshu["password"]
        (self.code,self.roleid)=login.login(self.host,self.username,self.password)
        self.assertEquals(self.code,0)

if __name__=="__main__":
    unittest.main()


