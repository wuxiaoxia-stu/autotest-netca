
from selenium.webdriver.common.by import By
from .base_page import BasePage

#左侧菜单页面
class MenuPage(BasePage):
    
    pin_button_loc = (By.XPATH, "//div[contains(text(),'PIN码管理')]")
    business_button_loc = (By.XPATH, "//div[contains(text(),'业务受理')]")
    search_button_loc = (By.XPATH, "//div[contains(text(),'业务查询')]")
    count_button_loc = (By.XPATH, "//div[contains(text(),'统计管理')]")
    delete_button_loc = (By.XPATH, "//div[contains(text(),'删除证书')]")
    renewalSearch_button_loc = (By.XPATH, "//div[contains(text(),'续期业务匹配')]")
    infoExport_button_loc = (By.XPATH, "//div[contains(text(),'导出业务登记信息')]")
 
    def pin_button(self):
        self.element(*self.pin_button_loc).click()  

    def business_button(self):
        self.element(*self.business_button_loc).click()

    def search_button(self):
        self.element(*self.search_button_loc).click() 

    def count_button(self):
        self.element(*self.count_button_loc).click()

    def delete_button(self):
        self.element(*self.delete_button_loc).click()

    def renewalSearch_button(self):
        self.element(*self.renewalSearch_button_loc).click()

    def infoExport_button(self):
        self.element(*self.infoExport_button_loc).click()
               
    def deleteCert(self):
        '''删除证书'''
        self.delete_button()
        self.exe('deleteCert.exe')

