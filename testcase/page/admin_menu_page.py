
from selenium.webdriver.common.by import By
from .base_page import BasePage

#左侧菜单页面
class MenuPage(BasePage):
    
    businessCenter_button_loc = (By.XPATH, "//div[contains(text(),'业务中心管理')]")
    CA_button_loc = (By.XPATH, "//div[contains(text(),'CA接入管理')]")
    project_button_loc = (By.XPATH, "//div[contains(text(),'项目管理')]")
    template_button_loc = (By.XPATH, "//div[contains(text(),'证书模板管理')]")
    service_button_loc = (By.XPATH, "//div[contains(text(),'用户服务管理')]")
    role_button_loc = (By.XPATH, "//div[contains(text(),'角色权限管理')]")
    user_button_loc = (By.XPATH, "//div[contains(text(),'系统用户管理')]")
    
 
    def businessCenter_button(self):
        self.element(*self.businessCenter_button_loc).click()  

    def CA_button(self):
    	self.element(*self.CA_button_loc).click()

    def project_button(self):
    	self.element(*self.project_button_loc).click() 

    def template_button(self):
    	self.element(*self.template_button_loc).click()

    def service_button(self):
    	self.element(*self.service_button_loc).click()

    def role_button(self):
    	self.element(*self.role_button_loc).click()

    def user_button(self):
    	self.element(*self.user_button_loc).click()

