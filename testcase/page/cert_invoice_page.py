
from selenium.webdriver.common.by import By
from .base_page import BasePage

#发票页面
class InvoicePage(BasePage):
    #电子发票
    getPrice_button_loc = (By.LINK_TEXT, "自动获取")
    invoiceInfo_text_loc = (By.ID, "eInvoiceInfo_GHF_NSRSBH")
    invoiceSubmit_button_loc = (By.XPATH, "//span[contains(text(),'开具发票')]")
    invoiceCancel_button_loc = (By.XPATH, "//span[contains(text(),'取消')]")
    invoiceDownload_button_loc = (By.XPATH, "//span[contains(text(),'下载电子发票')]")
    uninvoice_button_loc = (By.XPATH, "//div[@id='paperInvoiceInfoDialog']/div[3]/span[contains(text(),'冲红')]")
    uninvoiceInfo_text_loc = (By.ID, "eInvoiceInfo_memo")
    '''纸质发票相关'''
    pupiao_check_loc = (By.XPATH, "//label[contains(text(),'纸质打印发票(普票)')]")
    invoiceCode_text_loc = (By.ID, "paperInvoiceCode-inputEl")
    invoiceNo_text_loc = (By.ID, "paperInvoiceNo")
    invoiceAmount_text_loc = (By.ID, "paperInvoiceAmount")
    zhuanpiao_check_loc = (By.XPATH, "//label[contains(text(),'纸质打印发票(专票)')]")
    dinge_check_loc = (By.XPATH, "//label[contains(text(),'普通定额发票')]")
    invoiceCode2_text_loc = (By.ID, "invoiceCode_10-inputEl")
    invoiceNo2_text_loc = (By.XPATH, "//div[@id='invoiceNoDiv_10']/div[2]/input")
    #作废
    pUninvoiceInfo_text_loc = (By.ID, "paperInvoiceMemo")
    pUninvoiceSubmit_button_loc = (By.XPATH, "//span[contains(text(),'确定')]")
    #冲红
    pUninvoice_button_loc = (By.ID, "deleteRadio")
    pUninvoiceInfo2_text_loc = (By.ID, "paperInvoiceMemo_newInfo")
    invoiceCodeNew_text_loc = (By.ID, "paperInvoiceCode_newInfo-inputEl")
    invoiceNoNew_text_loc = (By.ID, "paperInvoiceNo_newInfo")
    #重用
    pReuseInfo_text_loc = (By.ID, "quotaInvoiceMemo")
    pReuse_button_loc = (By.XPATH, "//span[contains(text(),'重用')]")

    #查看纸质发票
    paperInvoice_button_loc = (By.ID, "showPaperInvoiceInfoDialog")

    def getPrice_button(self):
        self.element(*self.getPrice_button_loc).click()

    def invoiceInfo_text(self, text):
        self.send_keys(*self.invoiceInfo_text_loc,text=text)        

    def invoiceSubmit_button(self):
        self.element(*self.invoiceSubmit_button_loc).click()

    def invoiceCancel_button(self):
        self.element(*self.invoiceCancel_button_loc).click()

    def invoiceDownload_button(self):
        self.element(*self.invoiceDownload_button_loc).click()

    def uninvoice_button(self):
        self.element(*self.uninvoice_button_loc).click()

    def uninvoiceInfo_text(self, text):
        self.element(*self.uninvoiceInfo_text_loc).send_keys(text)

    def pupiao_check(self):
        self.check(*self.pupiao_check_loc)

    def invoiceCode_text(self, text):
        self.send_keys(*self.invoiceCode_text_loc, text=text)

    def invoiceNo_text(self, text):
        self.send_keys(*self.invoiceNo_text_loc, text=text)         

    def invoiceAmount_text(self, text):
        self.send_keys(*self.invoiceAmount_text_loc, text=text) 

    def zhuanpiao_check(self):
        self.check(*self.zhuanpiao_check_loc)

    def dinge_check(self):
        self.check(*self.dinge_check_loc)

    def invoiceCode2_text(self, text):
        self.send_keys(*self.invoiceCode2_text_loc, text=text)

    def invoiceNo2_text(self, text):
        self.element(*self.invoiceNo2_text_loc).click()
        self.send_keys(*self.invoiceNo2_text_loc, text=text)  

    def paperInvoice_button(self):
        self.check(*self.paperInvoice_button_loc)

    def pUninvoiceSubmit_button(self):
        self.check(*self.pUninvoiceSubmit_button_loc)

    def pUninvoiceInfo_text(self, text):
        self.send_keys(*self.pUninvoiceInfo_text_loc, text=text)

    def pUninvoice_button(self):
        self.check(*self.pUninvoice_button_loc)

    def pUninvoiceInfo2_text(self, text):
        self.send_keys(*self.pUninvoiceInfo2_text_loc, text=text)

    def invoiceCodeNew_text(self, text):
        self.send_keys(*self.invoiceCodeNew_text_loc, text=text)

    def invoiceNoNew_text(self, text):
        self.send_keys(*self.invoiceNoNew_text_loc, text=text) 

    def pReuse_button(self):
        self.check(*self.pReuse_button_loc)

    def pReuseInfo_text(self, text):
        self.send_keys(*self.pReuseInfo_text_loc, text=text)

    def newEInvoice(self):
        """
        开电子发票
        """
        self.getPrice_button() #获取金额
        self.invoiceInfo_text('91320582570354804Y')
        self.invoiceSubmit_button() #提交
        msg = self.alert()
        if "失败" in msg :
            self.invoiceCancel_button()

    def downloadEInvoice(self, win):
        """
        输入：运行系统
        操作：下载电子发票
        """
        self.invoiceDownload_button()
        self.sleep(2)
        self.exe('download.exe ' + win + ' 电子发票')

    def newPupiao(self, invoiceNo, invoiceCode, invoiceAmount):
        '''
        输入：发票号码、发票代码、发票金额
        操作：开普票
        '''
        self.invoiceNo_text(invoiceNo)
        self.invoiceCode_text(invoiceCode)           
        self.invoiceAmount_text(invoiceAmount)
        self.invoiceSubmit_button() #提交
        self.alert()

    def newZhuanpiao(self, invoiceNo, invoiceCode, invoiceAmount):
        '''
        输入：发票号码、发票代码、发票金额
        操作：开专票
        '''
        self.invoiceNo_text(invoiceNo)
        self.invoiceCode_text(invoiceCode)           
        self.invoiceAmount_text(invoiceAmount)
        self.invoiceSubmit_button() #提交
        self.alert()

    def newDinge(self, invoiceNo, invoiceCode):
        '''
        输入：发票号码、发票代码，金额默认为10
        操作：开定额发票
        '''
        self.sleep()
        self.invoiceCode2_text(invoiceCode)
        self.invoiceNo2_text(invoiceNo)
        self.invoiceSubmit_button() #提交
        self.alert()