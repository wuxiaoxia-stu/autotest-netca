from selenium.webdriver.common.by import By
from .base_page import BasePage
from common.getemail import getEmailContent

class HomePage(BasePage):
	apply_button_loc = (By.XPATH, "//a[text()='证书申请']")
	application_button_loc = (By.XPATH, "//a[text()='应用开通']")
	guide_button_loc = (By.XPATH, "//a[text()='证书使用']")
	verifyEmail_text_loc = (By.XPATH, "//*[@id='home']/div/div[1]/span")
	title_text_loc = (By.XPATH, "//span[@id='titleName']")
	
	#证书申请
	def apply_button(self):
		self.element(*self.apply_button_loc).click()
		
	#应用开通
	def application_button(self):
		self.element(*self.application_button_loc).click()

	#证书使用
	def guide_button(self):
		self.element(*self.guide_button_loc).click()
		
	#查看未完成操作
	def incomplete_button(self):
		js="document.getElementById('inCompleteATag').click()"
		self.driver.execute_script(js)

	#验证邮箱提示
	def verifyEmail_text(self):
		return self.text(*self.verifyEmail_text_loc)

	# 返回标题名称
	def title_text(self):
		return self.text(*self.title_text_loc)

	#验证邮箱
	def verifyEmail(self):
		content = getEmailContent()
		url = None
		try:
			url = content.splitlines()[4].strip()
		except (AttributeError):
			raise Exception('获取的不是业务平台验证邮件')
		if url.startswith("http") == False:
			raise Exception('获取的不是业务平台验证邮件')
		self.open(url)
		return self.verifyEmail_text()
