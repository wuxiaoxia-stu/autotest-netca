
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置附件页面
class ProjectSetFilePage(BasePage):

    setFile_button_loc = (By.XPATH, "//span[contains(text(),'附件配置')]/../input")
    fileName_text_loc = (By.ID, 'reqFileInput')
    fileRequired_check_loc = (By.ID, 'requiredInput')
    fileSubmit_button_loc = (By.XPATH, "//div[@id='reqFileDialog']//span[contains(text(),'完成')]")

    def setFile_button(self):
        self.element(*self.setFile_button_loc).click()

    def fileName_text(self, text):
        self.send_keys(*self.fileName_text_loc, text=text) 

    def fileRequired_check(self):
        self.check(*self.fileRequired_check_loc)

    def fileSubmit_button(self):
        self.element(*self.fileSubmit_button_loc).click()
