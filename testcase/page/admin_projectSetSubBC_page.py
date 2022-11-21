
from selenium.webdriver.common.by import By
from .base_page import BasePage

#配置证书模板页面
class ProjectSetSubBCPage(BasePage):

    setSubBC_button_loc = (By.XPATH, "//span[contains(text(),'所属子业务中心')]/../input")
    subBCSubmit_button_loc = (By.XPATH, "//div[@id='businessCenterDialog']//span[contains(text(),'完成')]")

    def setSubBC_button(self):
        self.element(*self.setSubBC_button_loc).click()

    def subBCName_text(self, text):
        xpath = "//div[@id='businessCenterMultiCheckDiv']/label[contains(text(), '" + text + "')]/input"
        self.check(By.XPATH, xpath)

    def subBCSubmit_button(self):
        self.element(*self.subBCSubmit_button_loc).click()
