
import unittest, sys, os
from time import strftime
from testcase.common.mail import send_mail
from testcase.common.HTMLTestRunner import HTMLTestRunner


if __name__=='__main__':

    now = strftime("%Y-%m-%d %H_%M_%S")  #获取当前时间
    reportname = now + "report.html"     #拼接测试报告文件名称
    suite = unittest.defaultTestLoader.discover('./testcase', pattern = '*_case.py')   #运行testcase文件夹下以case结尾的py文件
    with open('./output/report/' + reportname, 'wb') as fb:
        runner = HTMLTestRunner(stream=fb, title="测试报告", description="用例执行情况", retry=1)
        #runner = unittest.TextTestRunner()
        runner.run(suite)
    
    
    #send_mail(reportname)
