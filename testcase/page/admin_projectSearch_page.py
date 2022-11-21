
from selenium.webdriver.common.by import By
from .base_page import BasePage

#项目查询页面
class ProjectSearchPage(BasePage):

    projectSearch_iframe_loc = 2   
    projectName_text_loc = (By.ID, "name")
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详情')]")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    projectNo_text_loc = (By.ID, "projectNumber")
    indi_button_loc = (By.XPATH, "//input[@value='个性化配置']")

    def projectSearch_iframe_in(self):
        self.iframe_in(self.projectSearch_iframe_loc)

    def projectSearch_iframe_out(self):
        self.iframe_out()   

    def projectName_text(self, text):
        self.element(*self.projectName_text_loc).send_keys(text)  

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()   

    def projectNo_text(self, text):
        self.element(*self.projectNo_text_loc).send_keys(text)
        
    def indi_button(self):
        self.element(*self.indi_button_loc).click() 