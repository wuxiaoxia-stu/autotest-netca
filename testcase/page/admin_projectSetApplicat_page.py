
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置应用页面
class ProjectSetApplicatPage(BasePage):

    setApplicat_button_loc = (By.XPATH, "//span[contains(text(),'证书应用')]/../input")
    template_select_loc = (By.ID, "application_certTemplateSelect")
    applicetFee_text_loc = (By.ID, "useFee")
    applicatSubmit_button_loc = (By.XPATH, "//div[@id='applicationDialog']//span[contains(text(),'完成')]")

    def setApplicat_button(self):
        self.element(*self.setApplicat_button_loc).click()

    def template_select(self, text):
        self.select(*self.template_select_loc, text=text)


    def applicetFee_text(self, text):
        self.send_keys(*self.applicetFee_text_loc, text=text)

    def applicatSubmit_button(self):
        self.element(*self.applicatSubmit_button_loc).click()
