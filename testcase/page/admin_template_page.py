
from selenium.webdriver.common.by import By
from .base_page import BasePage

#证书模板管理页面
class TemplatePage(BasePage):

    template_iframe_loc = 2
    addTemplate_button_loc = (By.CLASS_NAME, 'add')
    templateName_text_loc = (By.NAME, "name")
    parentBusinessCenterName_text_loc = (By.ID, 'businessCenterId-inputEl')
    CAtemplateName_text_loc = (By.ID, 'externalTemplateId-inputEl')
    addCATemplate_button_loc = (By.XPATH, "//input[@value='添加CA模板']")
    addSubject_button_loc = (By.XPATH, "//input[@value='添加默认主题']")
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    detail_button_loc = (By.XPATH, "//a[contains(text(), '详细')]")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    dialog_close_button_loc = (By.XPATH, "//span[contains(text(),'关闭')]")

    def template_iframe_in(self):
        self.iframe_in(self.template_iframe_loc)

    def template_iframe_out(self):
        self.iframe_out()

    def addTemplate_button(self):
        self.element(*self.addTemplate_button_loc).click()

    def templateName_text(self, text):
        self.element(*self.templateName_text_loc).send_keys(text)

    def parentBusinessCenterName_text(self, text):
        self.element(*self.parentBusinessCenterName_text_loc).send_keys(text)  

    def CAtemplateName_text(self, text):
        self.element(*self.CAtemplateName_text_loc).send_keys(text)

    def addCATemplate_button(self):
        self.element(*self.addCATemplate_button_loc).click()

    def addSubject_button(self):
        self.element(*self.addSubject_button_loc).click()

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