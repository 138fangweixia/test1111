#coding=utf-8
import time
import unittest
import HTMLTestRunner

def all_case():
    #待执行用例的目录
    case_dir = "C:\\Users\\zhongda\\Desktop\\CRM\\crm_api\\case"
    testcase=unittest.TestSuite()
    #匹配所有test开头的脚本
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    testcase.addTest(discover)#直接加载
    print (testcase)
    return testcase

if __name__=="__main__":
    nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")

    report_path = "C:\\Users\\zhongda\\Desktop\\CRM\\crm_api\\report\\%s"%nowtime + "result.html"
    fp = open(report_path,"wb")
    runner= HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'CRM项目接口测试报告',description=u'用例执行情况如下：')
    runner.run(all_case())
    fp.close()
