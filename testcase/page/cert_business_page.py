
from selenium.webdriver.common.by import By
from .base_page import BasePage

#业务受理
class BusinessPage(BasePage):
    
    business_frame_loc = 2
    new_button_loc = (By.ID, "createNewUserBtn")
    old_button_loc = (By.XPATH, "//input[@value='根据插入的key查找用户']")
    selectUser_button_loc = (By.XPATH, "//table/tbody/tr[3]/td/div")
    submit_button_loc = (By.XPATH, "//input[@value='受理']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def business_frame_in(self):
        """
        进入业务受理iframe
        """
        self.iframe_in(self.business_frame_loc)

    def business_frame_out(self):
        """
        退出业务受理iframe
        """
        self.iframe_out()    
 
    def new_button(self):
        """
        点击创建新用户
        """
        self.element(*self.new_button_loc).click()  

    def old_button(self):
        """
        点击根据插入的key查找用户
        """
        self.element(*self.old_button_loc).click()

    def submit_button(self):
        """
        点击受理
        """
        self.element(*self.submit_button_loc).click()

    def close_button(self):
        """
        关闭业务受理菜单
        """
        self.element(*self.close_button_loc).click()

    def selectCert(self, n):
        """       
        输入：第n个证书
        操作：选择第n个证书
        """
        xpath = "//table/tbody/tr[" + str(1 + 3*n) + "]/td/div"
        self.element(By.XPATH, xpath).click()              

    def selectBusiness(self, business):
        """
        输入：证书业务
        操作：选择对应证书业务
        """
        xpath = "//input[@title='" + business + "']"
        self.element(By.XPATH, xpath).click()

    def acceptBusiness(self, business, n=0):
        """
        输入：证书业务，选择第n个证书
        操作：受理证书业务
        如果是新申请，后1个参数不需要填写
        """
        if business == "证书申请":
            self.new_button()
        else:
            self.old_button()
            self.sleep()
            self.selectCert(n)
            self.selectBusiness(business)
            self.submit_button()

    def selectUser_button(self):
        """选择用户"""
        self.element(*self.selectUser_button_loc).click()  