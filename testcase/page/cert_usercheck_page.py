
from selenium.webdriver.common.by import By
from .base_page import BasePage

#自助服务受理页面
class UserCheckPage(BasePage):
   
    check_frame_loc = 2
    check_button_loc = (By.LINK_TEXT, '自助服务受理')
    #业务单号输入框
    reqID_text_loc = (By.ID, "reqId")
    #批处理号输入框
    batchID_text_loc = (By.ID, "batchRequestId")
    search_button_loc = (By.ID, 'selectssReqBtn')
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")
    #业务页面
    submit_button_loc = (By.XPATH,"//input[@id='btn_accept']")
    goCheck_button_loc = (By.XPATH, "//div[@id='getRequestByIdDialogBox']//div//a")
    continueCheck_button_loc = (By.XPATH, "//div[@id='getRequestByIdDialogBox']//div[2]//a")
    #验证邮箱按钮
    verify_button_loc = (By.XPATH, "//input[@id='validEmailBtn']")
    getResult_button_loc = (By.XPATH, "//input[@id='getValidEmailBtn']")
    result_text_loc = (By.XPATH, "//*[@id='validEmailResult']")
    #推广码
    promoCode_text_loc = (By.XPATH, "//input[@title='推广码']")


    def check_frame_in(self):
        self.iframe_in(self.check_frame_loc)

    def check_frame_out(self):
        self.iframe_out()

    def check_button(self):
        self.element(*self.check_button_loc).click()

    def detail_button(self):
        self.element(*self.detail_button_loc).click()  

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def reqID_text(self, text):
        self.send_keys(*self.reqID_text_loc, text=text)

    def batchID_text(self, text):
        self.send_keys(*self.batchID_text_loc, text=text)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def goCheck_button(self):
        self.element(*self.goCheck_button_loc).click()

    def continueCheck_button(self):
        self.element(*self.continueCheck_button_loc).click()

    def verify_button(self):
        self.element(*self.verify_button_loc).click()

    def getResult_button(self):
        self.element(*self.getResult_button_loc).click()

    def result_text(self):
        return self.text(*self.result_text_loc)

    def promoCode_text(self):
        return self.element(*self.promoCode_text_loc).get_attribute('value')

    def checkBusiness(self, business_number):
        self.reqID_text(business_number)
        self.search_button()
        self.detail_button()
        self.submit_button()
        self.goCheck_button()

    def checkBusinessByBatchID(self, batchID):
        self.batchID_text(batchID)
        self.search_button()
        self.detail_button()
        self.submit_button()
        self.continueCheck_button()
        self.submit_button()
        self.continueCheck_button()
        self.submit_button()
        self.goCheck_button()
