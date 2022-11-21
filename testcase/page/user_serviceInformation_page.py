from selenium.webdriver.common.by import By
from .base_page import BasePage

class ServiceInformationPage(BasePage):
	agree_button_loc = (By.XPATH, "//input[@id='chooseBtn']")
	back_button_loc = (By.XPATH, "//input[@value='上一步']")
	#收费
	#第一行
	firstMonth_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[2]/td[1]")
	firstFee_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[2]/td[2]")
	# 第二行
	secondMonth_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[3]/td[1]")
	secondFee_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[3]/td[2]")
	# 第三行
	thirdMonth_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[4]/td[1]")
	thirdFee_text_loc = (By.XPATH, "//*[@id='feeTable']/tbody/tr[4]/td[2]")
	
	#点击确定按钮
	def agree_button(self):
		self.element(*self.agree_button_loc).click()
		
	#点击上一步按钮
	def back_button(self):
		self.element(*self.back_button_loc).click()

	def firstMonth_text(self):
		return self.text(*self.firstMonth_text_loc)

	def firstFee_text(self):
		return self.text(*self.firstFee_text_loc)

	def secondMonth_text(self):
		return self.text(*self.secondMonth_text_loc)

	def secondFee_text(self):
		return self.text(*self.secondFee_text_loc)

	def thirdMonth_text(self):
		return self.text(*self.thirdMonth_text_loc)

	def thirdFee_text(self):
		return self.text(*self.thirdFee_text_loc)

	#南网定制费用
	def returnFee(self):
		Month1 = self.firstMonth_text()
		Fee1 = self.firstFee_text()
		Month2 = self.secondMonth_text()
		Fee2 = self.secondFee_text()
		Month3 = self.thirdMonth_text()
		Fee3 = self.thirdFee_text()
		return [[Month1,Fee1],[Month2,Fee2],[Month3,Fee3]]