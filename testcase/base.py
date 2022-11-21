
from time import sleep, strftime
import unittest
import sys, os, platform, random
from functools import wraps
from selenium import webdriver
from common.data import read_data
from common.config import read_config
from common.screenshot import screenshot
from common.log import write_log

class Base(unittest.TestCase):

	driver = webdriver.Ie()
	ip = read_config('url','ip')
	n = read_config('login','num')
	password = read_config('login','password')	
	data_admin = read_data('admin.csv')
	data_cert = read_data('cert.csv')
	data_org = read_data('user_danwei.csv')
	data_staff = read_data('user_staff.csv')
	data_per = read_data('user_geren.csv')
	win = platform.release()
	now = strftime("%Y%m%d%H%M")
	operator = ''

	project = '自动化测试项目'
	#template = random.choice(['自动化测试-12SM2个人', '自动化测试-12SM2单位', '自动化测试-12RSA2048个人', '自动化测试-12RSA2048单位', '自动化测试-12RSA2048员工', '自动化测试-12SM2员工'])
	template = '自动化测试-12SM2单位'
	CAproject = '换CA自动化测试项目'
	subBusinessCenterName = '迁移测试业务中心'
	BusinessCenterName_sz = '自动化测试-深圳质监子业务中心'
	firstBusinessCenterName = '自动化测试-中信建投初审业务中心'
	secondBusinessCenterName = '自动化测试-中信建投复审业务中心'
	infoRegProject = '业务登记信息自动化测试项目' #业务登记信息自动化测试项目
	infoRegtemplate = '云南电力员工证书' #业务登记信息自动化测试模板
	project_sz = '深圳质监项目'
	template_sz = '深圳质监机构证书'
	project_zx = '中信建投项目'
	template_zx = '中信建投-新浪'	

	if '192.168.0.59' in ip or 'wxbpms' in ip:
		#newCAtemplate = random.choice(['110CA-SM2员工证书', '110CA-SM2机构证书', '110CA-SM2个人证书'])
		newCAtemplate = '110CA-SM2机构证书'
		parentBusinessCenterName = '公司业务根中心'
	elif '192.168.200.208' in ip:
		newCAtemplate = random.choice(['110CA-SM2员工证书', '110CA-SM2机构证书', '110CA-SM2个人证书', '110CA-RSA员工证书'])
		parentBusinessCenterName = '业务管理中心'
	elif '192.168.0.67' in ip or '192.168.0.50' in ip:
		newCAtemplate = random.choice(['110CA-SM2员工证书', '110CA-SM2机构证书'])
		parentBusinessCenterName = '顶级测试业务中心'

	
	def sleep(self, time=1):
		sleep(time)

	def screenshot(self, picturename):
		self.sleep()
		screenshot(picturename)

	def write_log(self, level, message):
		'''
		输入：日志级别(debug、info、warning、error、critical)，日志信息
		操作：写入日志
		'''
		write_log(level, message)

	def skip_dependon(depend=""):
	    """
	    :输入: 依赖的用例函数名，默认为空
	    :操作: 依赖用例执行失败则不执行当前用例
	    """
	    def wraper_func(test_func):
	        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
	        def inner_func(self):
	            if depend == test_func.__name__:
	                raise ValueError("{} cannot depend on itself".format(depend))
	            # print("self._outcome", self._outcome.__dict__)
	            # 此方法适用于python3.4 +
	            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
	            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
	            failures = str([fail[0] for fail in self._outcome.result.failures])
	            errors = str([error[0] for error in self._outcome.result.errors])
	            skipped = str([error[0] for error in self._outcome.result.skipped])
	            flag = (depend in failures) or (depend in errors) or (depend in skipped)
	            if failures.find(depend) != -1:
	                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
	                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
	                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
	                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
	            elif errors.find(depend) != -1:
	                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
	            elif skipped.find(depend) != -1:
	                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
	            else:
	                test = test_func
	            return test(self)
	        return inner_func
	    return wraper_func

	'''


	@classmethod
	def tearDown(cls):
		pass
		#cls.driver.quit()
	'''

