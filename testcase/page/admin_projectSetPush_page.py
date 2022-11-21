
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置LDAP页面
class ProjectSetPushPage(BasePage):

    setLDAP_button_loc = (By.ID, 'ldapConfigBtn')
    LDAPIp_text_loc = (By.ID, 'ldapHost')
    LDAPPort_text_loc = (By.ID, 'ldapPort')
    LDAPLogin_text_loc = (By.ID, 'ldapLoginDN')
    LDAPPassword_text_loc = (By.ID, 'ldapPassword')
    LDAPSubmit_button_loc = (By.XPATH, "//div[@id='ldapConfigDialog']//span[contains(text(),'保存')]")
    LDAP_check_loc = (By.XPATH, "//input[@name='certPusherImpls' and @value='1']")

    def setLDAP_button(self):
        self.element(*self.setLDAP_button_loc).click()

    def LDAPIp_text(self, text):
        self.element(*self.LDAPIp_text_loc).send_keys(text)

    def LDAPPort_text(self, text):
        self.element(*self.LDAPPort_text_loc).send_keys(text)

    def LDAPLogin_text(self, text):
        self.element(*self.LDAPLogin_text_loc).send_keys(text)        

    def LDAPPassword_text(self, text):
        self.element(*self.LDAPPassword_text_loc).send_keys(text)

    def LDAPSubmit_button(self):
        self.element(*self.LDAPSubmit_button_loc).click()

    def LDAP_check(self):
        self.element(*self.LDAP_check_loc).click()    
