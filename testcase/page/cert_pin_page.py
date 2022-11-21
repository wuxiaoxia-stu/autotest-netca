
from selenium.webdriver.common.by import By
from .base_page import BasePage

#PIN码管理菜单
class PinPage(BasePage):
    
    pin_frame_loc = 2
    adminPin_button_loc = (By.LINK_TEXT, "初始化管理员PIN")
    getAdminPin_button_loc = (By.XPATH, "//input[@value='平台获取']")
    generate_button_loc = (By.XPATH, "//input[@value='生成PIN码']")
    pinNum_text_loc = (By.ID, "pinNum")
    set_button_loc = (By.XPATH, "//input[@value='设置PIN码']")
    print_button_loc = (By.ID, 'isPrintM')
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def pin_iframe_in(self):
        """
        进入PIN码管理iframe
        """
        self.iframe_in(self.pin_frame_loc)

    def pin_iframe_out(self):
        """
        退出
        """
        self.iframe_out()    
 
    def adminPin_button(self):
        """
        进入初始化管理员PIN页面
        """
        self.element(*self.adminPin_button_loc).click()  

    def getAdminPin_button(self):
        """
        点击获取平台管理员PIN
        """
        self.element(*self.getAdminPin_button_loc).click()

    def generate_button(self):
        """
        生成随机新管理员PIN
        """
        self.element(*self.generate_button_loc).click() 

    def pinNum_text(self, text):
        """
        输入新用户PIN
        """
        self.element(*self.pinNum_text_loc).send_keys(text)

    def set_button(self):
        """
        点击设置PIN
        """
        self.element(*self.set_button_loc).click()

    def print_button(self):
        """
        点击取消打印密码信封
        """
        self.element(*self.print_button_loc).click()

    def close_button(self):
        """
        关闭PIN码管理菜单
        """
        self.element(*self.close_button_loc).click()



