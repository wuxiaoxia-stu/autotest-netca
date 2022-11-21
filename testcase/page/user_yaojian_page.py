from selenium.webdriver.common.by import By
from .base_page import BasePage

class YaojianPage(BasePage):
	yaojian_button_loc = (By.XPATH, "//*[@id='mCSB_1_container']/div/div[1]")
	submit_button_loc = (By.XPATH, "//*[@id='enterprise_confirm']")

	def yaojian_button(self):
		self.element(*self.yaojian_button_loc).click()

	def submit_button(self):
		self.element(*self.submit_button_loc).click()

	def chooseService(self):
		old_window = self.driver.current_window_handle
		self.yaojian_button()
		self.submit_button()
		self.closeIE()
		self.to_new_window(old_window)