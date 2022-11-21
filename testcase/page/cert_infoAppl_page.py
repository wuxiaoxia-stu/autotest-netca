
from selenium.webdriver.common.by import By
from .base_page import BasePage
import win32api, win32con

#业务信息
class InfoApplPage(BasePage):  
   
    getGeren_button_loc = (By.ID, "getLinkManInfoByUserInfoBtn")
    getDanwei_button_loc = (By.ID, "getLinkmanByIdBtn")
    getYuangong_button_loc = (By.ID, "getLatestLinkmanByOrgIdBtn")
    submit_button_loc = (By.XPATH, "//input[@value='提交']")

    '''应用相关'''
    appl_button_loc = (By.ID, "applicationIdCan0")
    endtime_button_loc = (By.ID, "appEndTimeCan0")
    endtime_frame_loc = 14
    endtimeHour_text_loc = (By.XPATH, "//input[@class='tB']")
    endtimeSubmit_button_loc = (By.XPATH, "//input[@value='确定']")
    month_text_loc = (By.ID, "intervalCan0")

  
    def getGeren_button(self):
        self.element(*self.getGeren_button_loc).click()  

    def getDanwei_button(self):
        self.element(*self.getDanwei_button_loc).click() 

    def getYuangong_button(self):
        self.element(*self.getYuangong_button_loc).send_keys(' ')
        #self.element(*self.getYuangong_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def appl_button(self):
        self.element(*self.appl_button_loc).click() 

    def endtime_button(self):
        self.element(*self.endtime_button_loc).click() 

    def endtime_frame_in(self):
        self.iframe_in(self.endtime_frame_loc)

    def endtime_frame_out(self):
        self.driver.switch_to.parent_frame() 

    def endtimeHour_text(self, text): 
        self.element(*self.endtimeHour_text_loc).click()
        win32api.keybd_event(50,0,0,0) 
        win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(51,0,0,0) 
        win32api.keybd_event(51,0,win32con.KEYEVENTF_KEYUP,0)

    def endtimeSubmit_button(self):
        self.element(*self.endtimeSubmit_button_loc).click()        

    def month_text(self, text): 
        self.element(*self.month_text_loc).send_keys(text)

    def getInfo(self, template):
        """
        输入：模板
        操作：获取经办人信息
        """
        if '个人' in template:
            self.getGeren_button()
        elif '单位' in template:
            self.getDanwei_button()
        elif '员工' in template:
            self.getYuangong_button()
    
