
from selenium.webdriver.common.by import By
from .base_page import BasePage

#第三方接口通信日志页面
class InterfacePage(BasePage):

    interface_frame_loc = 2
    more_button_loc = (By.LINK_TEXT, '详细')
    return_button_loc = (By.XPATH, "//input[@value='返回']")

    selectAll_button_loc = (By.ID, 'selectAll')
    batchAudit_button_loc = (By.XPATH, "//input[@value='批量审计']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    

    def interface_frame_in(self):
        self.iframe_in(self.interface_frame_loc)

    def interface_frame_out(self):
        self.iframe_out()    

    def more_button(self):
        self.element(*self.more_button_loc).click()

    def return_button(self):
        self.element(*self.return_button_loc).click()

    def selectAll_button(self):
        self.element(*self.selectAll_button_loc).click()

    def batchAudit_button(self):
        self.element(*self.batchAudit_button_loc).click()


    def close_button(self):
        self.element(*self.close_button_loc).click()

