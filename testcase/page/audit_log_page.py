
from selenium.webdriver.common.by import By
from .base_page import BasePage

#日志管理页面
class LogPage(BasePage):

    log_iframe_loc = 2
    queryType_select_loc = (By.ID, 'queryType')
    fileName_text_loc = (By.ID, 'filePath-inputEl')
    reset_button_loc = (By.XPATH, "//input[@value='重置偏移量']")
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    download_button_loc = (By.XPATH, "//input[@value='下载选中日志']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def log_iframe_in(self):
        self.iframe_in(self.log_iframe_loc)

    def log_iframe_out(self):
        self.iframe_out()

    def queryType_select(self, text):
        self.select(*self.queryType_select_loc, text=text)

    def fileName_text(self, text):
        self.send_keys(*self.fileName_text_loc, text=text)

    def reset_button(self):
        self.element(*self.reset_button_loc).click()

    def search_button(self):
        self.element(*self.search_button_loc).click()
        
    def download_button(self):
        self.element(*self.download_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()