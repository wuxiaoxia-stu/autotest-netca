
from selenium.webdriver.common.by import By
from .base_page import BasePage

#业务中心管理页面
class BusinessCenterPage(BasePage):
    
    businessCenter_iframe_loc = 2
    #添加
    addBusinessCenter_button_loc = (By.CLASS_NAME, 'add')
    #业务中心名称
    businessCenterName_text_loc = (By.NAME, 'name') 
    parentBusinessCenterName_text_loc = (By.NAME, 'parentId-inputEl')
    organization_text_loc = (By.NAME, 'organization')
    submit_button_loc = (By.XPATH, "//input[@value='添加']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    #查询
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    #详细
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")
    #修改
    submitModify_button_loc = (By.XPATH, "//input[@value='修改']")

    def businessCenter_iframe_in(self):
        self.iframe_in(self.businessCenter_iframe_loc)

    def businessCenter_iframe_out(self):
        self.iframe_out()

    def addBusinessCenter_button(self):
        self.element(*self.addBusinessCenter_button_loc).click()

    def businessCenterName_button(self):
        self.element(*self.businessCenterName_text_loc).click()

    def businessCenterName_text(self, text):
        self.element(*self.businessCenterName_text_loc).send_keys(text)

    def parentBusinessCenterName_text(self, text):
        self.element(*self.parentBusinessCenterName_text_loc).send_keys(text)

    def organization_text(self, text):
        self.element(*self.organization_text_loc).send_keys(text)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()
        
    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()

    def submitModify_button(self):
        self.element(*self.submitModify_button_loc).click()
