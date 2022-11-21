
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

#业务审核页面
class CheckResultPage(BasePage):
   
    '''审核成功弹窗'''
    tip_text_loc = (By.ID, "successTips")#安装结果
    tipSM2_text_loc = (By.ID, "reissueCertSuccessTips")#SM2证书安装结果
    tipCheck_text_loc = (By.XPATH, "//div[@id='afterAcceptanceDialog']//strong")#审核结果
    tipInvoice_text_loc = (By.ID, "addInvoiceMemo")#开票结果
    tipExpress_text_loc = (By.ID, "orderSpan")#下单结果
    tipSeal_text_loc = (By.ID, "sealAutoInstallTips")#电子印章安装结果

    newInvoice_button_loc = (By.XPATH, "//a[contains(text(),'开具发票')]")
    modifyInvoice_button_loc = (By.XPATH, "//a[contains(text(),'修改发票')]")
    express_button_loc = (By.XPATH, "//a[contains(text(),'下单')]")#下单
    
    SM2_button_loc = (By.ID, "reissueCertBtn")#办理SM2证书
    seal_button_loc = (By.ID, "signSealLink")#电子印章
    continue_button_loc = (By.XPATH, "//span[contains(text(),'继续受理')]")#继续受理
    coutinueCheck_button_loc = (By.ID, "reviewReqInBatch")
          
    def tip_text(self):
        self.sleep()
        return self.text(*self.tip_text_loc)

    def tipSM2_text(self):
        temp = self.text(*self.tipSM2_text_loc)
        if temp:
            return temp
        else:
            return self.tipSM2_text()

    def tipCheck_text(self):
        return self.text(*self.tipCheck_text_loc)    

    def tipInvoice_text(self):
        return self.text(*self.tipInvoice_text_loc)   

    def tipExpress_text(self):
        return self.text(*self.tipExpress_text_loc)   

    def tipSeal_text(self):
        return self.text(*self.tipSeal_text_loc)  
        
    def newInvoice_button(self):
        self.element(*self.newInvoice_button_loc).click()       

    def modifyInvoice_button(self):
        self.check(*self.modifyInvoice_button_loc)

    def express_button(self):
        self.element(*self.express_button_loc).click()

    def SM2_button(self):
        self.element(*self.SM2_button_loc).click() 
 
    def continue_button(self):
        self.sleep(2)
        self.element(*self.continue_button_loc).click()

    def coutinueCheck_button(self):
        self.sleep(2)
        self.element(*self.coutinueCheck_button_loc).click()


    def SM2_button(self):
        self.element(*self.SM2_button_loc).click() 

    def seal_button(self):
        self.element(*self.seal_button_loc).click() 
        

    def registerSM2(self):
        '''申请SM2证书'''
        self.sleep(2)
        self.SM2_button() #点击办理    
        self.sleep(2)            
        self.alert() #确认                
        self.alert() #已有证书确认
        self.sleep(2)
        self.alert()
        self.sleep(2)

