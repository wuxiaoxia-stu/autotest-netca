from selenium.webdriver.common.by import By
from .base_page import BasePage
import win32api, win32con

#业务登记信息
class InfoRegisterPage(BasePage):  

	customId_text_loc = (By.ID, "customId") #用户ID
	tradeOrgName_text_loc = (By.ID, "tradeOrgName") #电力交易系统单位名称
	tradeAccount_text_loc = (By.ID, "tradeAccount") #电力交易系统账号
	certApplyDate_button_loc = (By.ID, "certApplyDate") #证书申请时间
	receiveDate_button_loc = (By.ID, "receiveDate") #证书交付时间
	bindChangeDate_button_loc = (By.ID, "bindChangeDate") #系统账号绑定变更时间
	bindChangeReason_text_loc = (By.ID, "bindChangeReason") #系统账号绑定变更理由
	unbindChangeDate_button_loc = (By.ID, "unbindChangeDate") #原证书绑定解绑时间
	registrationProjectMemo_text_loc = (By.ID, "registrationProjectMemo") #备注

	date_frame_loc = 13 #日期控件
	dateSubmit_button_loc = (By.ID, "dpOkInput") #日期控件上的‘确认’按钮

	def customId_text(self, text): 
		self.element(*self.customId_text_loc).send_keys(text)
	
	def tradeOrgName_text(self, text): 
		self.element(*self.tradeOrgName_text_loc).send_keys(text)

	def tradeAccount_text(self, text): 
		self.element(*self.tradeAccount_text_loc).send_keys(text)

	def certApplyDate_button(self): 
		self.element(*self.certApplyDate_button_loc).click()  

	def receiveDate_button(self): 
		self.element(*self.receiveDate_button_loc).click()  

	def bindChangeDate_button(self): 
		self.element(*self.bindChangeDate_button_loc).click()  

	def bindChangeReason_text(self, text): 
		self.element(*self.bindChangeReason_text_loc).send_keys(text)

	def unbindChangeDate_button(self): 
		self.element(*self.unbindChangeDate_button_loc).click()  

	def registrationProjectMemo_text(self, text): 
		self.element(*self.registrationProjectMemo_text_loc).send_keys(text)    

	def date_frame_in(self):
		self.iframe_in(self.date_frame_loc)

	def date_frame_out(self):
		self.driver.switch_to.parent_frame()      

	def dateSubmit_button(self): 
		self.element(*self.dateSubmit_button_loc).click()     

	'''点击日期控件的‘确认’按钮'''
	def dateSubmit(self):
		self.date_frame_in()
		self.dateSubmit_button()
		self.date_frame_out()