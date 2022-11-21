
from selenium.webdriver.common.by import By
from .base_page import BasePage

#左侧菜单页面
class MenuPage(BasePage):
    
    manage_button_loc = (By.XPATH, "//div[contains(text(),'审计管理')]")
    log_button_loc = (By.XPATH, "//div[contains(text(),'日志管理')]")
    interface_button_loc = (By.XPATH, "//div[contains(text(),'第三方接口通信日志')]")

    def manage_button(self):
        self.element(*self.manage_button_loc).click()  

    def log_button(self):
        self.element(*self.log_button_loc).click()

    def interface_button(self):
        self.element(*self.interface_button_loc).click() 

