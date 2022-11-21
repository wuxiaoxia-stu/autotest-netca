from selenium.webdriver.common.by import By
from .base_page import BasePage

#证书安装页面
class InstallPage(BasePage):

    install_frame_loc = 2    
    install_button_loc = (By.LINK_TEXT, '证书安装')
    installCert_button_loc = (By.LINK_TEXT, '安装证书')
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def install_frame_in(self):
        self.iframe_in(self.install_frame_loc)

    def install_frame_out(self):
        self.iframe_out()

    def install_button(self):
        self.element(*self.install_button_loc).click()

    def installCert_button(self):
        self.element(*self.installCert_button_loc).click() 

    def close_button(self):
        self.element(*self.close_button_loc).click()

    def installCert(self):
        self.installCert_button()
        self.exe('inputpassword.exe')
        self.sleep()
        self.alert()