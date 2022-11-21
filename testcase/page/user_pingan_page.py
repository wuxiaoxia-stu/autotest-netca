from selenium.webdriver.common.by import By
from .base_page import BasePage

class PinganPage(BasePage):
	unicode_text_loc = (By.XPATH,"//input[@id='userunicode']")
	username_text_loc = (By.XPATH, "//input[@id='userunicodename']")
	apply_button_loc = (By.XPATH, "//input[@value='单位证书新申请']")

	#填写用户ID
	def unicode_text(self,text):
		self.input(*self.unicode_text_loc,text=text)

	#填写用户姓名
	def username_text(self,text):
		self.input(*self.username_text_loc,text=text)

	#点击新申请按钮
	def apply_button(self):
		self.element(*self.apply_button_loc).click()

	#新申请
	def apply(self,unicode,username):
		self.unicode_text(unicode)
		self.username_text(username)
		self.apply_button()