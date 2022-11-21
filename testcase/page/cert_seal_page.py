
from selenium.webdriver.common.by import By
from .base_page import BasePage

#PIN码管理菜单
class SealPage(BasePage):
    
    seal_frame_loc = 2
    seal_button_loc = (By.LINK_TEXT, "电子印章")
    delete_button_loc = (By.XPATH, "//input[@value='删除印章']")
    upload_button_loc = (By.ID, "SWFUpload_0")
    writeSeal_button_loc = (By.XPATH, "//input[@value='写入印章']")

    def seal_iframe_in(self):
        self.iframe_in(self.pin_frame_loc)

    def seal_iframe_out(self):
        self.iframe_out()
 
    def seal_button(self):
        self.element(*self.seal_button_loc).click()

    def delete_button(self):
        self.element(*self.delete_button_loc).click()

    def deleteSeal(self):
        self.delete_button()
        self.alert()
        self.exe("inputpassword.exe")
        self.alert()

    def upload_button(self):
        self.element(*self.upload_button_loc).click()
        
    def uploadFile(self, win, fileName):
        '''
        输入：运行系统
        操作：上传附件
        '''
        if win == '10':
            self.upload_button()
        self.sleep()                
        self.exe('upload_type2.exe ' + win + ' ' + fileName + ' 0')

    def writeSeal_button(self):
        self.element(*self.writeSeal_button_loc).click()