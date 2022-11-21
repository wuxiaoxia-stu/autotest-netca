from selenium.webdriver.common.by import By
from .base_page import BasePage

class ApplyPage(BasePage):

    Selectapply_text = (By.XPATH, "//input[contains(@id,'checkbox')]")

    def Selectapply_Text (self):
        self.element(*self.Selectapply_text).click()
        return self.alert()