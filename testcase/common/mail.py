
import yagmail
from .config import read_config

def send_mail(reportname):
	receiver = read_config('email', 'receiver')#
	#链接邮箱服务器
	yag = yagmail.SMTP( user="1379668375@qq.com", password="ytoeraajewsmiajf", host='smtp.qq.com')
	# 发送邮件
	yag.send(receiver.split('；'), '自动化测试报告', ['自动化测试已完成，测试报告见附件'], './output/report/' + reportname)

if __name__=='__main__': 
	send_mail('report.html')