from selenium.webdriver.common.by import By
from .base_page import BasePage
class GuidePage(BasePage):
    #第一条指引
    firstGuide_button_loc = (By.XPATH,"//*[@id='indexBodyRight']/div/div[3]/ul/li[1]/span[1]/a")
    #指引标题
    guideTitle_text_loc = (By.XPATH,"//b[@id='guideTitle']")
    #指引内容
    guideContent_text_loc = (By.XPATH,"//*[@id='guideMessageDiv']/p")

    def firstGuide_button(self):
        self.element(*self.firstGuide_button_loc).click()

    def guideTitle_text(self):
        return self.text(*self.guideTitle_text_loc)

    def guideContent_text(self):
        return self.text(*self.guideContent_text_loc)