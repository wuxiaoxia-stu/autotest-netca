
from selenium.webdriver.common.by import By
from .base_page import BasePage

'''
脚本信息：登录页面
编写人：郭丹颖
编写时间：2018-5
'''
class LoginPage(BasePage):
    
    #登录按钮
    login_button_loc = (By.CLASS_NAME, 'bodySiginBtn')
    #业务中心输入框
    businessCenter_text_loc = (By.ID, 'loginBusinessCenterId-inputEl')
    #确认按钮
    submit_button_loc = (By.XPATH, "//span[contains(text(),'确定')]")

    def login_button(self):
        """
        点击登录按钮
        """
        self.element(*self.login_button_loc).click()  

    def businessCenter_text(self, text):
        """
        在业务中心输入框输入text
        """
        self.send_keys(*self.businessCenter_text_loc, text=text)

    def submit_button(self):
        """
        点击确认按钮
        """
        self.element(*self.submit_button_loc).click()  

    def loginCert(self, ip, bc, n, password):
        """
        输入：登录ip，业务中心，操作员证书，密码
        操作：打开ip对应的证书业务系统，选择操作员输入密码登录，进入业务中心
        """
        self.url = ip + '/certbpms/login.jsp'
        self.open(self.url)
        self.login_button()
        self.exe('login.exe '+n+' '+password)
        self.sleep()
        try: #单业务中心时不需要选择
            self.businessCenter_text(bc)
            self.submit_button()  
        except:
            pass

    def loginAdmin(self, ip, n, password):
        """
        输入：登录ip，操作员证书，密码
        操作：打开ip对应的综合管理系统，选择操作员输入密码登录
        """
        self.url = ip + '/adminbpms/login.jsp'
        self.open(self.url)
        self.login_button()
        self.exe('login.exe '+n+' '+password)
        self.sleep()

    def loginAudit(self, ip, n, password):
        """
        输入：登录ip，操作员证书，密码
        操作：打开ip对应的审计系统，选择操作员输入密码登录
        """
        self.url = ip + '/auditbpms/login.jsp'
        self.open(self.url)
        self.login_button()
        self.exe('login.exe '+n+' '+password)
        self.sleep()        