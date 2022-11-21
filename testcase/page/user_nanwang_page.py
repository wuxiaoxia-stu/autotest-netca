from selenium.webdriver.common.by import By
from .base_page import BasePage

class NanwangPage(BasePage):
	orgBase_button_loc = (By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]")
	orgCompose_button_loc = (By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[2]")
	staffBase_button_loc = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]")
	staffCompose_button_loc = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]")

	def orgBase_button(self):
		self.element(*self.orgBase_button_loc).click()

	def orgCompose_button(self):
		self.element(*self.orgCompose_button_loc).click()

	def staffBase_button(self):
		self.element(*self.staffBase_button_loc).click()

	def staffCompose_button(self):
		self.element(*self.staffCompose_button_loc).click()