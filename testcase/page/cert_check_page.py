
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

#业务审核页面
class CheckPage(BasePage):
   
    check_frame_loc = 2
    check_button_loc = (By.LINK_TEXT, '业务审核')
    #业务单号输入框
    reqID_text_loc = (By.ID, "reqId") 
    search_button_loc = (By.ID, 'selectReviewBtn') 
    detail_button_loc = (By.XPATH, "//a[contains(text(),'详细')]")        
    #业务单号信息
    reqIDInfo_text_loc = (By.XPATH, "//table[@id='approveInfoTable']/tbody/tr[2]/td[2]") 
    #按钮-导出申请表
    export_button_loc = (By.ID, 'fillAndDownPDFBtn') 
    #按钮-没有条形码
    nokey_button_loc = (By.ID, "noKeyNumber")
    #货到付款
    cod_button_loc = (By.XPATH, "//label[contains(text(),'货到付款')]")
    #按钮-业务修改
    modify_button_loc = (By.ID, "btn_jumpToModRequest")
    submit_button_loc = (By.XPATH, "//input[@value='确认提交']")
    #按钮-返回业务受理？？？
    return_button_loc = (By.ID, "backToSelectPage")
    #返回按钮
    back_button_loc = (By.ID, "backToSelectBtn")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    #发票相关
    pupiao_check_loc = (By.XPATH, "//label[contains(text(),'纸质打印发票(普票)')]")
    invoiceCode_text_loc = (By.ID, "paperInvoiceCode-inputEl")
    invoiceNo_text_loc = (By.ID, "paperInvoiceNo")
    invoiceAmount_text_loc = (By.ID, "paperInvoiceAmount")
    zhuanpiao_check_loc = (By.XPATH, "//label[contains(text(),'纸质打印发票(专票)')]")
    dinge_check_loc = (By.XPATH, "//label[contains(text(),'普通定额发票')]")
    invoiceCode2_text_loc = (By.ID, "invoiceCode_10-inputEl")
    invoiceNo2_text_loc = (By.XPATH, "//div[@id='invoiceNoDiv_10']/div[2]/input")
    #预览印章图片
    viewSeal_button_loc = (By.XPATH,"//a[contains(text(),'预览')]")
    #操作员签名结果
    signResult_text_loc = (By.XPATH,"//span[contains(text(),'操作员签名有效')]")

    error_button_loc = (By.ID, "commonErrDialog_titleClose']")#关闭
    # 推广码
    promoCode_text_loc = (By.XPATH, "//td[@data-title='推广码']")

    #申请印章
    isNeedSeal_button_loc = (By.XPATH,"//input[@id='isNeedSealReq']")
    #印章名称
    sealName_text_loc = (By.XPATH, "//input[@id='sealRequestName']")



    def check_frame_in(self):
        self.iframe_in(self.check_frame_loc)

    def check_frame_out(self):
        self.iframe_out() 
        
    def export_button(self):
        self.element(*self.export_button_loc).click() 

    def nokey_button(self):
        self.check(*self.nokey_button_loc)

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def return_button(self):
        self.element(*self.return_button_loc).click()        

    def back_button(self):
        self.element(*self.back_button_loc).click()

    def cod_button(self):
        self.element(*self.cod_button_loc).click()

    def check_button(self):
        self.element(*self.check_button_loc).click() 

    def detail_button(self):
        self.element(*self.detail_button_loc).click()  

    def modify_button(self):
        self.element(*self.modify_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()

    def search_button(self):
        self.check(*self.search_button_loc)

    def reqID_text(self, text):
        self.send_keys(*self.reqID_text_loc, text=text)

    def reqIDInfo_text(self):
        return self.text(*self.reqIDInfo_text_loc)

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

    def viewSeal_button(self):
        self.element(*self.viewSeal_button_loc)

    def signResult_text(self):
        self.element(*self.signResult_text_loc)

    def promoCode_text(self):
        return self.text(*self.promoCode_text_loc)

    def isNeedSeal_button(self):
        self.element5s(*self.isNeedSeal_button_loc).click()

    def getSealName(self):
        return self.element(*self.sealName_text_loc).get_attribute("value")

    def error_button(self):
        self.sleep(4)
        self.element(*self.error_button_loc).click() 
        '''
        try:
            self.element(*self.error_button_loc).click() 
            print('11111111111111')
        except:
            pass
        else:
            
        '''
        self.submit_button()

    def checkBusiness(self, existCert=False,needSeal=False):
        """
        输入：是否已存在证书
        操作：业务审核,如果已存在证书，确认弹框
        """
        if(needSeal == False):
            try :
                js = "return $('#isNeedSealReq')[0].checked"  # 已经切换至iframe里面
                value =  self.driver.execute_script(js)
                if(value == True):
                    self.isNeedSeal_button()
            except:
                pass
        self.submit_button()       
        if(existCert):
            self.alert()
        self.exe('inputpassword.exe')

    def searchBusiness(self, reqID):
        """
        输入：业务单号
        操作：根据业务单号查询出待审核业务
        """
        self.reqID_text(reqID)
        self.search_button()

    def exportPDF(self, win):
        """
        输入：运行系统
        操作：导出业务申请表单
        """
        self.export_button()
        self.sleep(2)
        self.exe('download.exe ' + win + ' 业务审核导出的申请表')    
