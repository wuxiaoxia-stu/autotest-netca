
from selenium.webdriver.common.by import By
from .base_page import BasePage

#系统用户管理页面
class UserPage(BasePage):

    user_iframe_loc = 2

    #按钮-添加用户
    addUser_button_loc = (By.CLASS_NAME, 'add')
    #文本框-用户名称
    userName_text_loc = (By.NAME, "name")
    #选择框-用户类型
    userType_select_loc = (By.ID, 'type')
    #所属业务中心-左
    parentBusinessCenterName_select_loc1 = (By.ID, 'select1')
    #所属业务中心-右
    parentBusinessCenterName_select_loc2 = (By.ID, 'select2')
    #按钮-右移
    moveRight_button_loc = (By.XPATH, "//input[@value='＞＞']")
    #按钮-左移
    moveLeft_button_loc = (By.XPATH, "//input[@value='＜＜']")
    #文本框-证件类型
    identityType_select_loc = (By.NAME, "identityType")
    #文本框-证件号码
    identity_text_loc = (By.NAME, 'identity')
    #单选框
    setCert_check_loc = (By.ID, 'setCertCheckbox')
    #按钮-浏览
    file_button_loc = (By.NAME, "certFile")
    #按钮-完成
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    #按钮-下一步
    next_button_loc = (By.XPATH, "//input[@value='下一步']")    
    #按钮-查询
    search_button_loc = (By.XPATH, "//input[@value='查询']")
    #按钮-详细
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")
    #detail_button_loc = (By.LINK_TEXT, "详细")
    #选框-所有角色
    role_check_loc = (By.XPATH, "//input[@value='checkboxRole']")

    search_button_loc = (By.XPATH, "//input[@value='查询']")
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")  

    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def user_iframe_in(self):
        self.iframe_in(self.user_iframe_loc)

    def user_iframe_out(self):
        self.iframe_out()

    def addUser_button(self):
        self.element(*self.addUser_button_loc).click()

    def userName_text(self, text):
        self.element(*self.userName_text_loc).send_keys(text)

    def userType_select(self, text):
        self.select(*self.userType_select_loc, text=text) 

    def parentBusinessCenterName_select1(self, text):
        self.select(*self.parentBusinessCenterName_select_loc1, text=text)  

    def moveRight_button(self):
        self.element(*self.moveRight_button_loc).click()

    def parentBusinessCenterName_select2(self, text):
        self.select(*self.parentBusinessCenterName_select_loc2, text=text)  

    def moveLeft_button(self):
        self.element(*self.moveLeft_button_loc).click()

    def identityType_select(self, text):
        self.select(*self.identityType_select_loc, text=text)     

    def identity_text(self, text):
        self.element(*self.identity_text_loc).send_keys(text)

    def setCert_check(self):
        self.element(*self.setCert_check_loc).click()

    def file_button(self):
        self.double_click(*self.file_button_loc)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()

    def next_button(self):
        self.element(*self.next_button_loc).click()

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()

    def role_check(self):
        self.check(*self.role_check_loc)

    def detail_button(self):
        self.element(*self.detail_button_loc).click()    

    def submitM_button(self):
        self.element(*self.submitM_button_loc).click()

    def modifyUser(self, user, originalBusinessCenterName, goalBusinessCenterName):
        '''
        输入：用户名称、原业务中心、目标业务中心
        操作：根据用户名称查询，更改该用户所属业务中心和权限
        '''
        self.userName_text(user)
        self.search_button()
        self.detail_button()
        self.parentBusinessCenterName_select1(goalBusinessCenterName)
        self.moveRight_button()
        self.parentBusinessCenterName_select2(originalBusinessCenterName)
        self.moveLeft_button()
        self.next_button()
        self.role_check()
        self.submit_button()
        self.alert()  

    def uploadCert(self, fileName):
        '''上传用户签名证书'''
        self.file_button()     
        self.sleep()         
        self.exe('upload_type1.exe ' + fileName)