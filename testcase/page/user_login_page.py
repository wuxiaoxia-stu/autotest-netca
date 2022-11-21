from selenium.webdriver.common.by import By
from .base_page import BasePage

class UserLoginPage(BasePage):
	#普通登录页面
	loginPhone_text_loc = (By.XPATH, "//input[@id='validPhone2']")
	imgCode_text_loc = (By.XPATH, "//input[@id='imgValidCode']")
	phoneCode_text_loc = (By.XPATH, "//input[@name='validCode']")
	login2_button_loc = (By.XPATH, "//input[@id='verifyBtn2']")
	#东莞社保登录页面
	socialCode_text_loc = (By.XPATH, "//input[@name='4']")
	linkmanNum_text_loc = (By.XPATH, "//input[@name='20']")
	orgName_text_loc = (By.XPATH, "//input[@name='5']")
	login4_button_loc = (By.XPATH, "//input[@id='verifyBtn4']")
	#耗材登录页面
	linkmanName_text_loc = (By.XPATH, "//input[@name='21']")
	linkmanPhone_text_loc = (By.XPATH, "//input[@name='23']")
	#有旧业务弹窗
	goApply_button_loc = (By.XPATH, "//span[@id='commonDialog_cancel']")
	goFinish_button_loc = (By.XPATH,"//span[@id='commonDialog_confirm']")
	
	#填写用户手机号
	def loginPhone_text(self,text):
		self.element(*self.loginPhone_text_loc).send_keys(text)
	
	#填写图形验证码
	def imgCode_text(self,text):
		self.element(*self.imgCode_text_loc).send_keys(text)
	
	#填写手机验证码
	def phoneCode_text(self,text):
		self.element(*self.phoneCode_text_loc).send_keys(text)
	
	#点击登录2按钮
	def login2_button(self):
		self.element(*self.login2_button_loc).click()
		
	#填写统一社会信用代码
	def socialCode_text(self,text):
		self.element(*self.socialCode_text_loc).send_keys(text)
		
	#填写经办人身份证
	def linkmanNum_text(self,text):
		self.element(*self.linkmanNum_text_loc).send_keys(text)
		
	#填写单位名称
	def orgName_text(self,text):
		self.element(*self.orgName_text_loc).send_keys(text)
		
	#点击登录4按钮
	def login4_button(self):
		self.element(*self.login4_button_loc).click()
		
	#填写授权人名称
	def linkmanName_text(self,text):
		self.element(*self.linkmanName_text_loc).send_keys(text)
		
	#填写授权人手机号
	def linkmanPhone_text(self,text):
		self.element(*self.linkmanPhone_text_loc).send_keys(text)

	# 点击去新建业务
	def goApply_button(self):
		try:
			self.driver.find_element(*self.goApply_button_loc).click()
		except:
			pass

	def goFinish_button(self):
		try:
			self.driver.find_element(*self.goFinish_button_loc).click()
		except:
			pass
		
	#普通登录
	def loginUser(self,*org_value,apply=True):
		self.loginPhone_text(org_value[0][12])
		self.imgCode_text("1234")
		self.phoneCode_text("1234")
		self.login2_button()
		if apply :
			self.goApply_button()
	
	#登录东莞社保
	def loginDGSI(self,socialCode,linkmanNum,orgName):
		self.socialCode_text(socialCode)
		self.linkmanNum_text(linkmanNum)
		self.orgName_text(orgName)
		self.login4_button()
	
	#登录耗材
	def loginHaoCai(self,orgName,linkmanName,linkmanPhone):
		self.orgName_text(orgName)
		self.linkmanName_text(linkmanName)
		self.linkmanPhone_text(linkmanPhone)
		self.login4_button()