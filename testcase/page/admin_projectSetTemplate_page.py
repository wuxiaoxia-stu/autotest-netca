
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置证书模板页面
class ProjectSetTemplatePage(BasePage):

    setTemplate_button_loc = (By.XPATH, "//span[contains(text(),'证书模板配置')]/../input")
    templateSubmit_button_loc = (By.XPATH, "//div[@id='certTemplateDialog']//span[contains(text(),'完成')]")

    def setTemplate_button(self):
        self.element(*self.setTemplate_button_loc).click()

    def templateName_text(self, text):
        xpath = "//div[@id='certTemplateMultiCheckDiv']//label[contains(text(), '" + text + "')]/input"
        self.check(By.XPATH, xpath)

    def templateSubmit_button(self):
        self.element(*self.templateSubmit_button_loc).click()
