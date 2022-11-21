
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置快递费页面
class ProjectSetExpressPage(BasePage):

    setExpress_button_loc = (By.XPATH, "//span[contains(text(),'快递费')]/../input")
    expressFee0_button_loc = (By.ID, "expressFeeModeCheckbox0")
    expressFee1_button_loc = (By.ID, "expressFeeModeCheckbox1")
    expressFee2_button_loc = (By.ID, "expressFeeModeCheckbox2")
    needCert_button_loc = (By.ID, "isNeedCertbpms")
    expressSubmit_button_loc = (By.XPATH, "//div[@id='expressFeeDialog']//span[contains(text(),'完成')]")

    def setExpress_button(self):
        self.element(*self.setExpress_button_loc).click()

    def expressFee0_button(self):
        self.element(*self.expressFee0_button_loc).click()

    def expressFee1_button(self):
        self.element(*self.expressFee1_button_loc).click()

    def expressFee2_button(self):
        self.element(*self.expressFee2_button_loc).click()

    def needCert_button(self):
        self.element(*self.needCert_button_loc).click()

    def expressSubmit_button(self):
        self.element(*self.expressSubmit_button_loc).click()