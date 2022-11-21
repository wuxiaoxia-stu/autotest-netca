
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置证书有效期页面
class ProjectSetDataPage(BasePage):

    setData_button_loc = (By.XPATH, "//span[contains(text(),'证书有效期')]/../input")
    data2_button_loc = (By.ID, "2")
    fixMonth_text_loc = (By.ID, "fixMonth")
    dataSubmit_button_loc = (By.XPATH, "//div[@id='certDateDialog']//span[contains(text(),'完成')]")

    def setData_button(self):
        self.element(*self.setData_button_loc).click()

    def data2_button(self):
        self.element(*self.data2_button_loc).click()

    def fixMonth_text(self, text):
        self.element(*self.fixMonth_text_loc).send_keys(text)

    def dataSubmit_button(self):
        self.element(*self.dataSubmit_button_loc).click()
