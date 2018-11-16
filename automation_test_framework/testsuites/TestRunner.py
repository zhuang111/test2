# coding = utf-8
import unittest
import HTMLTestRunner
import os
import time
from testsuites.test_baidu_search import BaiduSearch


# suite = unittest.TestLoader().discover("testsuites")
suite = unittest.TestSuite()
classname = BaiduSearch
casename = 'test_login_enovia'
suite.addTest(classname(casename))
#报告路径
report_path = os.path.dirname(os.path.abspath('.'))+'/test-report/'

#获取当前时间
now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

#报告格式
report_name = report_path+now+'_HTMLTemplate.html'
fp = open(report_name,'wb+')

if __name__=='__main__':
    #执行用例
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'测试用例执行情况')
    runner.run(suite)