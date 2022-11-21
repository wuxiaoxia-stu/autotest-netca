
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置证书服务费页面
class ProjectSetCostPage(BasePage):

    setCost_button_loc = (By.XPATH, "//span[contains(text(),'证书服务费')]/../input")
    certFee_text_loc = (By.ID, "certServiceFee")
    costSubmit_button_loc = (By.XPATH, "//div[@id='certServiceFeeDialog']//span[contains(text(),'完成')]")

    def setCost_button(self):
        self.element(*self.setCost_button_loc).click()

    def certFee_text(self, text):
        self.send_keys(*self.certFee_text_loc, text=text)

    def costSubmit_button(self):
        self.element(*self.costSubmit_button_loc).click()
