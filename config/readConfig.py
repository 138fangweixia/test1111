# coding:utf-8
import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini") #cfg.ini的路径

#创建管理对象
conf = configparser.ConfigParser()

#读ini文件
conf.read(configPath,encoding="utf-8")

#获取email下smtp_server的值
smtp_server = conf.get("email", "smtp_server")
# print (smtp_server)

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")
