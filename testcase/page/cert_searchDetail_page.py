
from selenium.webdriver.common.by import By
from .base_page import BasePage

#业务查询页面
class SearchDetailPage(BasePage):
    
    addFile_button_loc = (By.NAME, 'addRequestFile')
    upload_button_loc = (By.ID, "SWFUpload_0")
    certInfo_button_loc = (By.ID, 'certInfoFoldButton')
    download_button_loc = (By.LINK_TEXT, '下载')
    return_button_loc = (By.XPATH, "//input[@value='返回']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
 
    def addFile_button(self):
        self.element(*self.addFile_button_loc).click()

    def upload_button(self):
        self.element(*self.upload_button_loc).click()

    def certInfo_button(self):
        self.element(*self.certInfo_button_loc).click()

    def download_button(self):
        self.element(*self.download_button_loc).click()

    def return_button(self):
        self.element(*self.return_button_loc).click()
    
    def close_button(self):
        self.element(*self.close_button_loc).click()

    def uploadFile(self, win, fileName):
        '''
        输入：运行系统
        操作：上传附件
        if win == '10':
            self.sleep()
            self.upload_button()        
        '''
        if win =='7':
            self.addFile_button()

            self.sleep()                
            self.exe('upload_type2.exe 7 ' + fileName + ' 0')