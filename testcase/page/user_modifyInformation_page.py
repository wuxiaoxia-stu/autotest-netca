from selenium.webdriver.common.by import By
from .base_page import BasePage

class ModifyInformationPage(BasePage):
	userName_text_loc = (By.XPATH,"//input[@id='userNameShow']")
	linkmanId_text_loc = (By.XPATH,"//input[@id='linkmanIdentityShow']")
	linkmanName_text_loc = (By.XPATH,"//input[@id='linkmanNameShow']")
	submit_button_loc = (By.XPATH,"//input[@value='提交']")
	submitRequest_button_loc = (By.XPATH,"//input[@value='提交证书请求']")
	sealName_text_loc = (By.XPATH,"//input[@id='sealName']")
	validmonth_select_loc = (By.XPATH,"//select[@id='month']")
	reqid_text_loc = (By.XPATH, "//span[@id='reqId']")
	
	#修改用户名称
	def userName_text(self,text):
		self.input(*self.userName_text_loc,text=text)
		
	#修改经办人证件号码
	def linkmanId_text(self,text):
		self.input(*self.linkmanId_text_loc,text=text)
		
	#修改经办人姓名
	def linkmanName_text(self,text):
		self.input(*self.linkmanName_text_loc,text=text)
		
	#点击提交按钮
	def submit_button(self):
		self.element(*self.submit_button_loc).click()
	
	#点击提交证书请求按钮
	def submitRequest_button(self):
		self.element(*self.submitRequest_button_loc).click()

	#填写印章名称
	def sealName_text(self, text):
		# self.input(*self.sealName_text_loc, text=text)
		js = "document.getElementById('sealName').setAttribute('value','" + text + "')"
		self.driver.execute_script(js)

	#有效期改为2年
	def validmonth_select(self):
		self.select(*self.validmonth_select_loc, text="24")

	#返回reqID
	def reqid_text(self):
		return self.text(*self.reqid_text_loc)
		
	#修改信息上传证书请求流程
	def mendifyInformation(self,*staff_value):
		self.sleep(1)
		self.userName_text(staff_value[0][11])
		self.linkmanId_text(staff_value[0][10])
		self.linkmanName_text(staff_value[0][11])
		self.submit_button()
		self.alert()
		self.submitRequest_button()
		self.exe('inputpassword.exe')
		self.alert()
		self.alert()