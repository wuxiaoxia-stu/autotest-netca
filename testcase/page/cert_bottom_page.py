
from selenium.webdriver.common.by import By
from .base_page import BasePage

#底部页面
class BottomPage(BasePage):
    

    bottom_text_loc = (By.XPATH, "//td[contains(text(),'欢迎您')]")
    bottom_frame_loc = 2

    def bottom_iframe_in(self):
        self.iframe_in(self.bottom_frame_loc)

    def bottom_iframe_out(self):
        self.iframe_out() 

    def bottom_text(self):
        return self.text(*self.bottom_text_loc)

