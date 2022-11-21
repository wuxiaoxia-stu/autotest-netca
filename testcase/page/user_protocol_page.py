from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProtocolPage(BasePage):
	agree_button_loc = (By.XPATH, "//input[@id='agreeButton']")
	back_button_loc = (By.XPATH, "//input[@value='返回首页']")
	title_text_loc = (By.XPATH,"//*[@id='protocolDiv']/div[1]")
	quit_button_loc = (By.XPATH,"//a[@id='logoutLink']")
	
	#点击同意按钮
	def agree_button(self):
		self.element(*self.agree_button_loc).click()
		
	#点击返回首页按钮
	def back_button(self):
		self.element(*self.back_button_loc).click()

	#返回标题名称
	def title_text(self):
		return self.text(*self.title_text_loc)

	#退出登录
	def quit_button(self):
		self.element(*self.quit_button_loc).click()