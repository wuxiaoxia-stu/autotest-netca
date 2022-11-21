
from selenium.webdriver.common.by import By
from .base_page import BasePage

#审计管理页面
class ManagePage(BasePage):

    manage_iframe_loc = 2
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def manage_iframe_in(self):
        self.iframe_in(self.manage_iframe_loc)

    def manage_iframe_out(self):
        self.iframe_out()

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()