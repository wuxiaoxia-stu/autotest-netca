
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

#业务审核页面
class ExpressPage(BasePage):
   
      
    expressSubmit_button_loc = (By.ID, "orderDialog_goToPlaceOrderBtn")
    #按钮-打印订单成功后的关闭窗口
    expressClose_button_loc = (By.XPATH, "//div[@id='showMailNoDialog']//span[contains(text(),'关闭窗口')]")

    def expressSubmit_button(self):
        self.element(*self.expressSubmit_button_loc).click()

    def expressClose_button(self):
        self.element(*self.expressClose_button_loc).click()

    def getExpress(self, win):
        '''
        输入：运行系统
        操作：下单、打单
        '''
        self.expressSubmit_button()
        self.alert()        
        self.sleep()
        self.alert()
        self.exe('print.exe ' + win + ' ' + '快递单') 
        self.expressClose_button()
