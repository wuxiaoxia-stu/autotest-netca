
from selenium.webdriver.common.by import By
from .base_page import BasePage

#角色权限管理页面
class RolePage(BasePage):

    role_iframe_loc = 2
    #菜单-添加
    addRole_button_loc = (By.CLASS_NAME, 'add')
    #角色名称
    roleName_text_loc = (By.NAME, "name")
    #所属业务中心
    parentBusinessCenterName_text_loc = (By.ID, 'businessCenterId-inputEl')   
    #完成
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    
    next_button_loc = (By.XPATH, "//input[@value='下一步']")#下一步 
    busiOperation_button_loc = (By.XPATH, "//input[@value='4']")#业务操作权限
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    detail_button_loc = (By.XPATH, "//a[contains(text(),'修改')][2]")  
    submitM_button_loc = (By.XPATH, "//input[@value='更改']")

    def role_iframe_in(self):
        self.iframe_in(self.role_iframe_loc)

    def role_iframe_out(self):
        self.iframe_out()

    def addRole_button(self):
        self.element(*self.addRole_button_loc).click()

    def roleName_text(self, text):
        self.element(*self.roleName_text_loc).send_keys(text)
        self.element(*self.roleName_text_loc).click()

    def parentBusinessCenterName_text(self, text):
        self.element(*self.parentBusinessCenterName_text_loc).send_keys(text)
        self.element(*self.parentBusinessCenterName_text_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()
    
    def close_button(self):
        self.element(*self.close_button_loc).click()

    def next_button(self):
        self.element(*self.next_button_loc).click()

    def busiOperation_button(self):
        self.element(*self.busiOperation_button_loc).click()

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()    

    def submitM_button(self):
        self.element(*self.submitM_button_loc).click()