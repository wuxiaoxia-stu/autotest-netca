from selenium.webdriver.common.by import By
from .base_page import BasePage

class ApplicationPage(BasePage):
	selectApply_select_loc = (By.XPATH, "//input[contains(@id,'checkbox')]")
	linkmanType_select_loc = (By.XPATH, "//select[@id='linkmanIdentityType']")
	linkmanId_text_loc = (By.XPATH, "//input[@id='linkmanIdentityShow']")
	linkmanName_text_loc = (By.XPATH, "//input[@id='linkmanNameShow']")
	linkmanPhone_text_loc = (By.XPATH, "//input[@id='linkmanPhoneShow']")
	linkmanEmail_text_loc = (By.XPATH, "//input[@id='linkmanEmailShow']")
	next_button_loc = (By.XPATH, "//input[@value='下一步']")
	veryfyCode_text_loc = (By.XPATH, "//input[@id='imgValidCodeText']")
	submit_button_loc = (By.XPATH, "//input[@value='提 交']")
	
	def selectApply_select(self):
		self.element(*self.selectApply_select_loc).click()
		
	def linkmanType_select(self,text):
		self.select(*self.linkmanType_select_loc, text)
		
	def linkmanId_text(self,text):
		self.element(*self.linkmanId_text_loc).send_keys(text)
		
	def linkmanName_text(self,text):
		self.element(*self.linkmanName_text_loc).send_keys(text)
		
	def linkmanPhone_text(self,text):
		self.element(*self.linkmanPhone_text_loc).send_keys(text)
		
	def linkmanEmail_text(self,text):
		self.element(*self.linkmanEmail_text_loc).send_keys(text)
		
	def next_button(self):
		self.element(*self.next_button_loc).click()
		
	def veryfyCode_text(self,text):
		self.element(*self.veryfyCode_text_loc).send_keys(text)
		
	def submit_button(self,text):
		self.element(*self.submit_button_loc).click()
		
	def applyApplication(self,*org_value):
		self.selectApply_select()
		self.alert()
		self.linkmanType_select(org_value[0][9])
		self.linkmanId_text(org_value[0][10])
		self.linkmanName_text(org_value[0][11])
		self.linkmanPhone_text(org_value[0][12])
		self.linkmanEmail_text(org_value[0][13])
		self.next_button()
		self.veryfyCode_text("1234")
		self.submit_button()
		self.alert()
		sleep(1)
		self.alert()