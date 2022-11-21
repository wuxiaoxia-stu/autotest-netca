
from selenium.webdriver.common.by import By
from .base_page import BasePage

#项目个性化页面
class ProjectIndiPage(BasePage):

    
    client_text_loc = (By.ID, "client")
    #刷卡
    cash_button_loc = (By.XPATH, "//div[@id='paidType']//input[@value='2']")
    #企业银联
    Alipay_button_loc = (By.XPATH, "//div[@id='paidType']//input[@value='11']")
    needService_button_loc = (By.ID, "hasSelfSevice")
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    


    def client_text(self, text):
        self.send_keys(*self.client_text_loc, text=text)    

    def cash_button(self):
        self.check(*self.cash_button_loc)

    def Alipay_button(self):
        self.check(*self.Alipay_button_loc)

    def needService_button(self):
        self.check(*self.needService_button_loc)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

