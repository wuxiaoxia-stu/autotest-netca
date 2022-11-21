from selenium.webdriver.common.by import By
from .base_page import BasePage
class PerUnionPayPage(BasePage):

    #卡号
    cardNum_text_loc = (By.XPATH, "//input[@id='cardNumber']")
    #下一步按钮
    nextPay_button_loc = (By.XPATH, "//input[@id='btnNext']")
    #姓名
    cardName_text_loc = (By.XPATH, "//input[@id='realName']")
    #证件号
    idCardNum_text_loc = (By.XPATH, "//input[@id='credentialNo']")
    #获取验证码按钮
    getCode_button_loc = (By.XPATH, "//input[@id='btnGetCode']")
    #验证码
    code_text_loc = (By.XPATH, "//input[@id='smsCode']")
    #支付
    pay_button_loc = (By.XPATH, "//input[@id='btnCardPay']")
    #继续访问
    overRideLink_button_loc = (By.XPATH, "//a[@id='overridelink']")

    def cardNum_text(self, cardNum):
        self.input(*self.cardNum_text_loc, text=cardNum)

    def nextPay_Button(self):
        self.element(*self.nextPay_button_loc).click()

    def cardName_text(self, cardName):
        self.element(*self.cardName_text_loc).send_keys(cardName)

    def idCardNum_text(self, idCardNum):
        self.element(*self.idCardNum_text_loc).send_keys(idCardNum)

    def getCode_Button(self):
        self.element(*self.getCode_button_loc).click()

    def pay_Button(self):
        self.element(*self.pay_button_loc).click()

    def code_text(self, code):
        self.element(*self.code_text_loc).send_keys(code)

    def overRideLink_button(self):
        try:
            self.element(*self.overRideLink_button_loc).click()
        except:
            pass

    def pay(self,old_window):
        self.to_new_window(old_window)
        self.overRideLink_button()
        self.cardNum_text("6216261000000000018")
        self.nextPay_Button()
        self.cardName_text("全渠道")
        self.idCardNum_text("341126197709218366")
        self.getCode_Button()
        self.code_text("111111")
        self.pay_Button()
        self.sleep()
        self.closeIE()

