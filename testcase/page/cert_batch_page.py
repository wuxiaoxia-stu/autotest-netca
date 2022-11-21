
from selenium.webdriver.common.by import By
from testcase.page.base_page import BasePage

#批量导入
class BatchPage(BasePage):
    batch_frame_loc = 2
    batch_button_loc = (By.LINK_TEXT, '批量处理')
    project_text_loc = (By.XPATH, "//input[@id='projectId-inputEl']") #项目名称
    template_text_loc = (By.XPATH, "//input[@id='templateId-inputEl']") #证书模板
    upload_button_loc = (By.XPATH, "//input[@id='fileTable']") #上传附件
    need_radio_loc = (By.XPATH, "//input[@value='true']") #需要自助服务
    summit_button_loc = (By.XPATH, "//input[@value='导入业务']")  # 导入业务
    goCheck_button_loc = (By.XPATH, "//span[@id='batchReviewDialog_gotoReviewBtn']")  #立即审核
    businessNum_text_loc = (By.XPATH, "//table[@id='reViewTable']//tbody//tr[1]//td[1]") #业务单号

    def batch_frame_in(self):
        self.iframe_in(self.batch_frame_loc)

    def batch_frame_out(self):
        self.iframe_out()

    def batch_button(self):
        self.element(*self.batch_button_loc).click()

    def project_text (self,key):
        self.element(*self.project_text_loc).send_keys(key)

    def template_text (self,key):
        self.element(*self.template_text_loc).clear()
        self.element(*self.template_text_loc).send_keys(key)

    def upload_button (self):
        self.double_click(*self.upload_button_loc)

    def need_radio (self):
        self.element(*self.need_radio_loc).click()

    def summit_button (self):
        self.element(*self.summit_button_loc).click()

    def goCheck_button (self):
        self.element(*self.goCheck_button_loc).click()

    def businessNum_text (self):
        business_number = self.element(*self.businessNum_text_loc).text
        return business_number
