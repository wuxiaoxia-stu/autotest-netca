
from selenium.webdriver.common.by import By
from .base_page import BasePage

#用户服务管理页面
class ServicePage(BasePage):

    service_iframe_loc = 2
    addService_button_loc = (By.CLASS_NAME, 'add')
    serviceName_text_loc = (By.NAME, "name")
    projectName_button_loc = (By.ID, 'ext-gen1037')
    templateName_text_loc = (By.ID, 'templateId-inputEl')
    feeMode_button_loc = (By.XPATH, "//input[@name='selfServiceFeeModeCertApply'and@value='2']")
    reqType_button_loc = (By.XPATH, "//input[@name='reqType'and@value='0']")
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    search_button_loc = (By.ID, 'btn_searchSelfService')
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    dialog_close_button_loc = (By.XPATH, "//span[contains(text(),'关闭')]")

    def service_iframe_in(self):
        self.iframe_in(self.service_iframe_loc)

    def service_iframe_out(self):
        self.iframe_out()

    def addService_button(self):
        self.element(*self.addService_button_loc).click()

    def serviceName_text(self, text):
        self.element(*self.serviceName_text_loc).send_keys(text)

    def projectName_text(self, text):
        self.element(*self.projectName_button_loc).click()
        self.li(text).click()

    def templateName_text(self, text):
        self.element(*self.templateName_text_loc).send_keys(text)

    def feeMode_button(self):
        self.element(*self.feeMode_button_loc).click()

    def reqType_button(self):
        self.element(*self.reqType_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()
        
    def close_button(self):
        self.element(*self.close_button_loc).click()

    def dialog_close_button(self):
        self.element(*self.dialog_close_button_loc).click()