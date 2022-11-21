import requests
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Org4SM2Page(BasePage):
	url_text_loc = (By.XPATH,"//input[@name='registerCertURL']")
	systemId_text_loc = (By.XPATH, "//input[@name='systemId']") 
	projectId_text_loc = (By.XPATH, "//input[@name='projectId']") 
	templateId_text_loc = (By.XPATH, "//input[@name='templateId']") 
	centerId_text_loc = (By.XPATH, "//input[@name='businessCenterId']") 
	p10_text_loc = (By.XPATH, "//*[@name='p10']")
	orgName_text_loc = (By.XPATH, "//input[@name='name']")
	orgType_text_loc = (By.XPATH, "//input[@name='identityType']")
	orgId_text_loc = (By.XPATH, "//input[@name='identity']")
	linkmanName_text_loc = (By.XPATH, "//input[@name='linkmanname']") 
	linkmanPhone_text_loc = (By.XPATH, "//input[@name='linkmanphone']")
	linkmanEmail_text_loc = (By.XPATH, "//input[@name='linkmanemail']")
	submit_button_loc = (By.XPATH, "//input[@value='提交']")
	
	def url_text(self,text):
		self.input(*self.url_text_loc,text=text)
		
	def systemId_text(self,text):
		self.input(*self.systemId_text_loc,text=text)
		
	def projectId_text(self,text):
		self.input(*self.projectId_text_loc,text=text)
		
	def templateId_text(self,text):
		self.input(*self.templateId_text_loc,text=text)
		
	def centerId_text(self,text):
		self.input(*self.centerId_text_loc,text=text)
		
	def p10_text(self):
		self.element(*self.p10_text_loc).clear()
	
	def orgName_text(self,text):
		self.input(*self.orgName_text_loc,text=text)
		
	def orgType_text(self,text):
		self.input(*self.orgType_text_loc,text=text)
		
	def orgId_text(self,text):
		self.input(*self.orgId_text_loc,text=text)
		
	def linkmanName_text(self,text):
		self.input(*self.linkmanName_text_loc,text=text)
		
	def linkmanPhone_text(self,text):
		self.input(*self.linkmanPhone_text_loc,text=text)

	def linkmanEmail_text(self,text):
		self.input(*self.linkmanEmail_text_loc,text=text)
		
	def submit_button(self):
		self.element(*self.submit_button_loc).click()
		
	def applyCert(self,certbpms_value,org_value):
		self.url_text(certbpms_value[0])
		self.systemId_text(certbpms_value[1])
		self.projectId_text(certbpms_value[2])
		self.templateId_text(certbpms_value[3])
		self.centerId_text(certbpms_value[4])
		self.p10_text()
		self.orgName_text(org_value[3])
		self.orgType_text("513")
		self.orgId_text(org_value[2])
		self.linkmanName_text(org_value[11])
		self.linkmanPhone_text(org_value[12])
		self.linkmanEmail_text(org_value[13])
		self.submit_button()
		while True:
			url = self.driver.current_url
			if "TestRegisterCert" in url:
				business_number = self.driver.find_element_by_xpath("//body").text.split('"')[3]
				break
		return business_number

	def postData(self,ip):
		url = ip + '/certbpms/RegisterCert.servlet'
		data = {
			'registerRequest': "{'systemId':'epoint','projectId':'P003220170622001','templateId':'T004001201904220001','businessCenterId':1,'cert':{'interval':12},'user':{'name':'NETCA','identityType':513,'identity':'91532301MA6K3MAKXN','countryName':'CN','province':'Guangdong','city':'Guangzhou','phone':'15626480142','address':'德安大厦','officialResidence':'德安大厦','email':'lier@cnca.net','organizationType':1,'organizationCode':'12345678'},'linkman':{'name':'da','identityType':2,'identity':'12345','phone':'13719099617','email':'zhangsan@cnca.net','address':'德安大厦'},'memo':'请填写备注信息'}",
			'signature': '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'}
		requests.packages.urllib3.disable_warnings()
		r = requests.post(url, verify=False, data=data)
		result = r.json()
		return result['reqId']