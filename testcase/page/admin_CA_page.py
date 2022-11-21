
from selenium.webdriver.common.by import By
from .base_page import BasePage

#CA接入管理页面
class CAPage(BasePage):

    CA_iframe_loc = 2
    CATemplate_button_loc = (By.CLASS_NAME, 'caTemplate') #菜单按钮
    addCATemplate_button_loc = (By.XPATH, "//input[@value='添加CA模板']")
    CATemplateName_text_loc = (By.ID, 'externalTemplateNameAdd')
    CATemplateId_text_loc = (By.ID, 'externalTemplateIdAdd')
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    CATemplateNameS_text_loc = (By.ID, 'externalTemplateName') 
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    detail_button_loc = (By.XPATH, "//a[contains(text(), '详细')]")
    CATemplateNameM_text_loc = (By.ID, 'externalTemplateNameMod') 
    submitM_button_loc = (By.XPATH, "//form[@name='caTemplateMod']//input[@value='完成']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def CA_iframe_in(self):
        self.iframe_in(self.CA_iframe_loc)

    def CA_iframe_out(self):
        self.iframe_out()

    #点击CA模版配置
    def CATemplate_button(self):
        self.element(*self.CATemplate_button_loc).click()

    def addCATemplate_button(self):
        self.element(*self.addCATemplate_button_loc).click()

    def CATemplateName_text(self, text):
        self.element(*self.CATemplateName_text_loc).send_keys(text)

    def CATemplateId_text(self, text):
        self.element(*self.CATemplateId_text_loc).send_keys(text)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def CATemplateNameS_text(self, text):
        self.element(*self.CATemplateNameS_text_loc).send_keys(text)

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()

    def CATemplateNameM_text(self, text):
        self.element(*self.CATemplateNameM_text_loc).send_keys(text)

    def submitM_button(self):
        self.element(*self.submitM_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()