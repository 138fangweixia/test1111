#coding:utf-8
import requests
import json
def login(host,u1,p1):
    url=host+"/sys/login"
    # url="https://crm-test.jingdaka.com/api/crm/sys/login"
    body={"username":u1,"password":p1}
    r=requests.post(url,json=body)
    print(r.json())
    code=r.json()['code']
    roleid=r.json()['data']['roleId']
    print(code)
    return code,roleid
