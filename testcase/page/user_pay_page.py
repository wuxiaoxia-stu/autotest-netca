__author__ = 'qiuju'
from selenium.webdriver.common.by import By
from .base_page import BasePage
class PayPage(BasePage):
    #--------------快递付款方式----------------
    #货到付款
    payOnDelivery_button_loc = (By.XPATH, "//input[@name='expressFeeMode' and @value='0']")
    #随业务支付
    payByBusiness_button_loc = (By.XPATH, "//input[@name='expressFeeMode' and @value='1']")
    #网证通支付
    payByNetca_button_loc = (By.XPATH, "//input[@name='expressFeeMode' and @value='2']")

    #-----------------发票类型------------------
    #普通定额发票
    normalInvoice_button_loc = (By.XPATH, "//input[@name='invoiceType' and @value='1']")
    #增值税发票
    vatInvoice_button_loc = (By.XPATH, "//input[@name='invoiceType' and @value='2']")
    #电子发票
    electronicInvoice_button_loc = (By.XPATH, "//input[@name='invoiceType' and @value='3']")

    #-----------------支付方式------------------
    #定期结算
    payRegular_button_loc = (By.XPATH, "//input[@name='paidType' and @value='1']")
    #现金
    payCash_button_loc = (By.XPATH, "//input[@name='paidType' and @value='2']")
    #支票
    cheque_button_loc = (By.XPATH, "//input[@name='paidType' and @value='3']")
    #银行转账
    bankTransfer_button_loc = (By.XPATH, "//input[@name='paidType' and @value='4']")
    #个人银联
    perUnionPay_button_loc = (By.XPATH, "//input[@name='paidType' and @value='5']")
    #企业银联
    orgUnionPay_button_loc = (By.XPATH, "//input[@name='paidType' and @value='11']")
    #支付宝
    aliPay_button_loc = (By.XPATH, "//input[@name='paidType' and @value='6']")

    #-----------------普通发票信息------------------
    #纳税人识别号
    taxpayerIdentifyNum_text_loc = (By.XPATH, "//input[@title='纳税人识别号']")
    #发票抬头
    invoiceTile_text_loc = (By.XPATH, "//input[@title='发票抬头']")
    #补全发票信息按钮
    fullMassage_button_loc = (By.XPATH, "//*[@id='fill_nvoice_btn']/td/span")
    #确定按钮
    confirmMassage_button_loc = (By.XPATH, "//span[@id='isFillDialog_confirm']")
    #购买方地址
    buyAddress_text_loc = (By.XPATH, "//input[@id='GHF_DZShow']")
    #购买方电话
    buyPhone_text_loc = (By.XPATH, "//input[@id='GHF_GDDHShow']")
    #购买方账号
    buyAccount_text_loc = (By.XPATH, "//input[@id='GHF_YHZHShow']")
    #-----------------银行转账信息------------------
    #付款账号
    transferNum_text_loc = (By.XPATH, "//input[@title='付款账号']")
    #付款账户名
    transferName_text_loc = (By.XPATH, "//input[@title='付款账户名']")
    #转账金额
    transferMoney_text_loc = (By.XPATH, "//input[@title='转账金额']")
    #付款日期
    transferDate_button_loc = (By.XPATH, "//input[@title='付款日期']")
    #今天----日期控件
    today_button_loc = (By.XPATH, "//input[@value='今天']")
    #日期控件所在iframe
    iframe_ifm_loc = (By.XPATH, "//iframe[contains(@src,'js/calendar/My97DatePicker.htm')]")

    #返回查询
    returnQuery_button_loc = (By.XPATH, "//input[@value='返回查询']")
    #提交
    submit_button_loc = (By.XPATH, "//input[@id='saveInfoBtn']")
    #保存（去结算）
    gotoSubmit_button_loc = (By.XPATH, "//input[@id='goToSubmitBtn']")
    #去支付
    confirm_button_loc = (By.XPATH,"//span[@id='isPayDialog_confirm']")

    #完成支付
    done_button_loc = (By.XPATH, "//input[@id='done']")

    #返回查询
    payBack_button_loc = (By.XPATH, "//input[@id='payReqOnlineBack']")

    #业务单号
    businessNumber_text_loc = (By.XPATH,"//*[@id='reqIdsText']")

    #付款金额
    fee_text_loc = (By.XPATH,"//span[@id='selectTotalFee']")

    #上传增值税附件
    file_button_loc = (By.XPATH, "//*[@id='reqFileTable']/tbody/tr[2]/td[2]/span/div[2]/object")

    #--------------快递付款方式----------------
    #货到付款
    def payOnDelivery_button(self):
        self.element(*self.payOnDelivery_button_loc).click()
    #随业务支付
    def payByBusiness_Button(self):
        self.element(*self.payByBusiness_button_loc).click()
    #网证通支付
    def payByNetca_button(self):
        self.element(*self.payByNetca_button_loc).click()

    #-----------------发票类型------------------
    #普通发票
    def normalInvoice_button(self):
        self.element(*self.normalInvoice_button_loc).click()
    #增值税发票
    def vatInvoice_button(self):
        self.element(*self.vatInvoice_button_loc).click()
    #电子发票
    def electronicInvoice_button(self):
        self.element(*self.electronicInvoice_button_loc).click()

    #---------------支付方式-------------------
    #定期结算
    def payRegular_button(self):
        self.element(*self.payRegular_button_loc).click()
    #现金
    def payCash_button(self):
        self.element(*self.payCash_button_loc).click()
    #支票
    def cheque_button(self):
        self.element(*self.cheque_button_loc).click()
    #银行转账
    def bankTransfer_button(self):
        self.element(*self.bankTransfer_button_loc).click()
    #个人银联
    def perUnionPay_button(self):
        self.element(*self.perUnionPay_button_loc).click()
    #企业银联
    def orgUnionPay_button(self):
        self.element(*self.orgUnionPay_button_loc).click()
    #支付宝
    def aliPay_button(self):
        self.element(*self.aliPay_button_loc).click()

    #-----------------普通发票信息------------------
    #纳税人识别号
    def taxpayerIdentifyNum_text(self, text):
        self.input(*self.taxpayerIdentifyNum_text_loc, text=text)
    #发票抬头
    def invoiceTile_text(self, text):
        self.input(*self.invoiceTile_text_loc, text=text)
    #补全发票信息按钮
    def fullMassage_button(self):
        self.element(*self.fullMassage_button_loc).click()
    #确定按钮
    def confirmMassage_button(self):
        self.element(*self.confirmMassage_button_loc).click()
    # 购买方地址
    def buyAddress_text(self,text):
        self.input(*self.buyAddress_text_loc,text=text)
    # 购买方电话
    def buyPhone_text(self,text):
        self.input(*self.buyPhone_text_loc,text=text)
    # 购买方账号
    def buyAccount_text(self,text):
        self.input(*self.buyAccount_text_loc,text=text)

    #-----------------银行转账信息------------------
    #付款账号
    def transferNum_text(self,text):
        self.input(*self.transferNum_text_loc, text=text)
    #付款账户名
    def transferName_text(self,text):
        self.input(*self.transferName_text_loc, text=text)
    #转账金额
    def transferMoney_text(self,text):
        self.input(*self.transferMoney_text_loc, text=text)
    #转账日期
    def transferDate_button(self):
        self.element(*self.transferDate_button_loc).click()
    #今天--日期控件
    def today_button(self):
        self.element(*self.today_button_loc).click()
    #日期控件所在iframe
    def iframe_ifm(self):
        return self.element(*self.iframe_ifm_loc)

    #返回查询
    def returnQuery_button(self):
         self.element(*self.returnQuery_button_loc).click()
    #提交
    def submit_button(self):
         self.element(*self.submit_button_loc).click()
    #保存（去结算）
    def gotoSubmit_button(self):
         self.element(*self.gotoSubmit_button_loc).click()

    #去支付
    def confirm_button(self):
        self.element(*self.confirm_button_loc).click()

    #完成支付
    def done_button(self):
        self.element(*self.done_button_loc).click()

    def payBack_button(self):
        self.element(*self.payBack_button_loc).click()

    #返回业务单号
    def businessNumber_text(self):
        content = self.text(*self.businessNumber_text_loc)
        return content.split()[1]

    #付款金额
    def fee_text(self):
        return self.text(*self.fee_text_loc)

    # 附件上传
    def file_button(self):
        self.element(*self.file_button_loc).click()

    #-----------------业务逻辑------------------
    #选择电子发票，填税号
    def chooseElectronicInvoice(self,*org_value):
        self.electronicInvoice_button()
        self.invoiceTile_text(org_value[0][3])
        self.taxpayerIdentifyNum_text(org_value[0][2])
        self.fullMassage_button()
        self.confirmMassage_button()
        self.buyAddress_text(org_value[0][7])
        self.buyPhone_text(org_value[0][12])
        self.buyAccount_text("0200079783")

    #选择增值税发票
    def chooseVatInvoice(self):
        self.vatInvoice_button()
        self.file_button()
        self.exe('upload_type2.exe 7 3.jpg 0')

    #选择银行转账
    def chooseBankTransfer(self):
        self.bankTransfer_button()
        self.transferNum_text("341126197709218366")
        self.transferName_text("全渠道")
        self.transferMoney_text("1010")
        self.transferDate_button()
        self.iframe_in(self.iframe_ifm())
        self.today_button()
        self.iframe_out()
        self.submit_button()
        self.alert()

    #定期结算
    def payRegular(self):
        self.payRegular_button()
        self.submit_button()
        self.alert()

    #现金
    def payCash(self):
        self.payCash_button()
        self.submit_button()
        self.alert()

    #企业网银
    def orgUnionPay(self):
        self.orgUnionPay_button()
        old_window = self.driver.current_window_handle
        self.gotoSubmit_button()
        self.confirm_button()
        return old_window

    #个人网银
    def perUnionPay(self):
        self.perUnionPay_button()
        old_window = self.driver.current_window_handle
        self.gotoSubmit_button()
        self.confirm_button()
        return old_window

    def finishPay(self,old_window):
        self.to_old_window(old_window)
        self.sleep(1)
        self.done_button()
        self.payBack_button()