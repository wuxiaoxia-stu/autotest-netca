
from selenium.webdriver.common.by import By
from .base_page import BasePage

#统计管理页面
class CountPage(BasePage):

    count_frame_loc = 2

    #查询统计分析模块
    count_button_loc = (By.CLASS_NAME, 'certStatistics') #查询统计分析模块
    project_select_loc = (By.ID, 'optionalProjectIds') #项目
    moveProj_button_loc = (By.XPATH, "//div[@id='projectsDiv']//input[@value='＞＞']")
    time_button_loc = (By.NAME, 'timePoint')
    time_frame_loc = 3
    today_button_loc = (By.ID, 'dpTodayInput')
    submit_button_loc = (By.ID, 'selectValidCertBtn')

    expire_button_loc = (By.XPATH, "//label[contains(text(),'到期证书量统计')]")
    expireTimeStart_button_loc = (By.NAME, 'expireTimeStart')
    oneYear_button_loc = (By.XPATH, "//a[contains(text(),'一年')]")

    business_button_loc = (By.XPATH, "//label[contains(text(),'证书业务量统计')]")
    BC_select_loc = (By.ID, 'opCenterIds')   
    moveBC_button_loc = (By.XPATH, "//div[@id='businessCentersDiv']//input[@value='＞＞']")
    allBusi_button_loc = (By.XPATH, "//div[@id='busiTypeDiv']//input[@value='全选']")
    moveBusi_button_loc = (By.XPATH, "//div[@id='busiTypeDiv']//input[@value='＞＞']")
    busiTimeStart_button_loc = (By.ID, 'successTimeStart')
    one_button_loc = (By.XPATH, "//td[contains(text(),'1')]")
    busiTimeSubmit_button_loc = (By.ID, 'dpOkInput')
    busiTimeEnd_button_loc = (By.ID, 'successTimeEnd')

    #导出结果
    export_button_loc = (By.ID, 'exportValidCertBtn')

    #发票统计
    invoiceCount_button_loc = (By.XPATH, "//a[contains(text(),'发票统计')]")
    invoiveCSubmit_button_loc = (By.ID, 'selectBtn') #查询

    #发票明细表统计
    invoiceDetail_button_loc = (By.XPATH, "//label[contains(text(),'发票明细表统计')]")
    #工作量统计
    workload_button_loc = (By.XPATH, "//a[contains(text(),'工作量统计')]")
    workloadExport_button_loc = (By.ID, 'exportWorkloadBtn') #导出

    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')
    
    def count_frame_in(self):
        self.iframe_in(self.count_frame_loc)

    def count_frame_out(self):
        self.iframe_out()

    def count_button(self):
        self.element(*self.count_button_loc).click()      

    def project_select(self, text):
        self.select(*self.project_select_loc, text=text)

    def moveProj_button(self):
        self.element(*self.moveProj_button_loc).click()  

    def time_button(self):
        self.element(*self.time_button_loc).click()

    def time_frame_in(self):
        self.iframe_in(self.time_frame_loc)

    def time_frame_out(self):
        self.driver.switch_to.parent_frame() 

    def today_button(self):
        self.element(*self.today_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def expire_button(self):
        self.element(*self.expire_button_loc).click()

    def expireTimeStart_button(self):
        self.element(*self.expireTimeStart_button_loc).click()   
        
    def oneYear_button(self):
        self.element(*self.oneYear_button_loc).click()   

    def business_button(self):
        self.element(*self.business_button_loc).click() 

    def BC_select(self, text):
        self.select(*self.BC_select_loc, text=text)

    def moveBC_button(self):
        self.element(*self.moveBC_button_loc).click()        

    def allBusi_button(self):
        self.element(*self.allBusi_button_loc).click() 

    def moveBusi_button(self):
        self.element(*self.moveBusi_button_loc).click() 

    def busiTimeStart_button(self):
        self.element(*self.busiTimeStart_button_loc).click() 

    def one_button(self):
        self.element(*self.one_button_loc).click() 

    def busiTimeSubmit_button(self):
        self.element(*self.busiTimeSubmit_button_loc).click() 

    def busiTimeEnd_button(self):
        self.element(*self.busiTimeEnd_button_loc).click() 

    def close_button(self):
        self.element(*self.close_button_loc).click()

    def invoiceCount_button(self):
        self.element(*self.invoiceCount_button_loc).click()

    def invoiveCSubmit_button(self):
        self.element(*self.invoiveCSubmit_button_loc).click()

    def invoiveExport_button(self):
        js="document.getElementById('exportValidCertBtn').click()"
        self.driver.execute_script(js)    

    def invoiceDetail_button(self):
        self.element(*self.invoiceDetail_button_loc).click()  

    def export_button(self):
        self.element(*self.export_button_loc).click()           

    def workload_button(self):
        self.element(*self.workload_button_loc).click()  

    def workloadExport_button(self):
        #self.element(*self.workloadExport_button_loc).click()
        js="document.getElementById('exportWorkloadBtn').click()"
        self.driver.execute_script(js)