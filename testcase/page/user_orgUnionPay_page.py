__author__ = 'qiuju'
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from testcase.common.cbbb2bpay import cbbb2bpay
class OrgUnionPayPage(BasePage):

    #继续访问
    overRideLink_button_loc = (By.XPATH, "//a[@id='overridelink']")

    # -----------------订单信息------------------
    #订单号
    orderid_text_loc = (By.XPATH,"//*[@id='wrapper']/div/div[1]/ul/li[1]/ul/li[2]/span")
    #订单金额
    fee_text_loc = (By.XPATH,"//*[@id='wrapper']/div/div[1]/ul/li[2]/ul/li[2]/span/i")

    # -----------------模拟支付页面-----------------
    #订单号
    ordid_text_loc = (By.XPATH,"//input[@id='orderNumber']")
    #付款金额
    amount_text_loc = (By.XPATH,"//input[@id='amount']")
    #提交
    submit_button_loc = (By.XPATH,"//*[@id='payPageForm']/label[16]/input")
    #关闭页面
    close_button_loc = (By.XPATH,"//input[@id='closeBtn']")

    def overRideLink_button(self):
        try:
            self.element(*self.overRideLink_button_loc).click()
        except:
            pass

    def orderid_text(self):
        return self.text(*self.orderid_text_loc)

    def fee_text(self):
        return self.text(*self.fee_text_loc)

    def ordid_text(self,text):
        self.input(*self.ordid_text_loc,text=text)

    def amount_text(self,text):
        self.input(*self.amount_text_loc,text=text)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()

    def pay(self,old_window,ip):
        self.to_new_window(old_window)
        #self.overRideLink_button()
        orderid = self.orderid_text()
        fee = self.fee_text()
        self.driver.close()
        cbbb2bpay(ip, orderid, fee)
        '''
        payurl = ip + "/paySimulator/index"
        self.closeIE()
        self.driver = webdriver.Chrome()
        self.open(payurl)
        self.ordid_text(orderid)
        self.amount_text(fee)
        self.submit_button()
        self.close_button()
        self.driver.close()
        '''