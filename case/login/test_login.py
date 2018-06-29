#coding:utf-8
import requests
import unittest
from case.login import login

class Test_login(unittest.TestCase):

    u''' crm系统登录模块'''
    def setUp(self):
        self.host="https://crm-test.jingdaka.com/api/crm"

    def test01(self):
        u''' 运营主管正确帐号密码登录'''
        self.username="yunying1@jingdaka.com"
        self.password="admin123"
        (self.code,self.roleid)=login.login(self.host,self.username,self.password)
        self.assertEquals(self.code,0)
        self.assertEquals(self.roleid,4)

    def test02(self):
        u''' 普通运营正确帐号密码登录'''
        self.username="yifan@jingdaka.com"
        self.password="yifan123"
        (self.code,self.roleid)=login.login(self.host,self.username,self.password)
        self.assertEquals(self.code,0)
        self.assertEquals(self.roleid,5)

    def test03(self):
        u''' 销售主管正确帐号密码登录'''
        self.username="salemanager@jingdaka.com"
        self.password="admin123"
        (self.code,self.roleid)=login.login(self.host,self.username,self.password)
        self.assertEquals(self.code,0)
        self.assertEquals(self.roleid,3)

    def test04(self):
        u''' 普通销售正确帐号密码登录'''
        self.username="kangyong@jingdaka.com"
        self.password="kangyong"
        (self.code,self.roleid)=login.login(self.host,self.username,self.password)
        self.assertEquals(self.code,0)
        self.assertEquals(self.roleid,6)



if __name__=="__main__":
    unittest.main()


