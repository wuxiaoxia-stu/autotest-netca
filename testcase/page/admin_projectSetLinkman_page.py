
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置默认经办人页面
class ProjectSetLinkmanPage(BasePage):

    setLinkman_button_loc = (By.XPATH, "//span[contains(text(),'默认经办人配置')]/../input")
    renewalType_button_loc = (By.ID, 'linkmanUsage_0')
    unlockType_button_loc = (By.ID, 'linkmanUsage_1')
    identity_text_loc = (By.XPATH, "//input[@title='经办人证件号码']")
    name_text_loc = (By.XPATH, "//input[@title='经办人姓名']")
    phone_text_loc = (By.XPATH, "//input[@title='经办人手机号']")
    email_text_loc = (By.XPATH, "//input[@title='经办人邮箱']")
    address_text_loc = (By.XPATH, "//textarea[@title='经办人地址']")
    linkmanSubmit_button_loc = (By.XPATH, "//div[@id='projectLinkman']//span[contains(text(),'确定')]")

    def setLinkman_button(self):
        self.element(*self.setLinkman_button_loc).click()

    def renewalType_button(self):
        self.element(*self.renewalType_button_loc).click()

    def unlockType_button(self):
        self.element(*self.unlockType_button_loc).click()

    def identity_text(self, text):
        self.element(*self.identity_text_loc).click()
        self.element(*self.identity_text_loc).send_keys(text)  

    def name_text(self, text):
        self.element(*self.name_text_loc).click()
        self.element(*self.name_text_loc).send_keys(text)  

    def phone_text(self, text):
        self.element(*self.phone_text_loc).click()
        self.element(*self.phone_text_loc).send_keys(text)  

    def email_text(self, text):
        self.element(*self.email_text_loc).click()
        self.element(*self.email_text_loc).send_keys(text)  

    def address_text(self, text):
        self.element(*self.address_text_loc).send_keys(text)  

    def linkmanSubmit_button(self):
        self.element(*self.linkmanSubmit_button_loc).click()
