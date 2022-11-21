
from selenium.webdriver.common.by import By
from .base_page import BasePage

#业务查询页面
class SearchPage(BasePage):
    
    search_frame_loc = 2
    searchBusiness_button_loc = (By.XPATH, "//div[@id='conditionDiv']/div[1]/div[@class='foldButton']") #业务查询条件
    parentBC_text_loc = (By.ID, "businessCenterId-inputEl")
    project_text_loc = (By.ID, "projectId-inputEl")
    template_text_loc = (By.ID, "templateId-inputEl")
    searchCert_button_loc = (By.XPATH, "//div[@id='conditionDiv']/div[3]/div[@class='foldButton']") #证书查询条件
    certType_select_loc = (By.NAME, "certType")    
    searchUser_button_loc = (By.XPATH, "//div[@id='conditionDiv']/div[5]/div[@class='foldButton']") #用户查询条件
    userName_text_loc = (By.NAME, "userName")    
    searchLinkman_button_loc = (By.XPATH, "//div[@id='conditionDiv']/div[7]/div[@class='foldButton']") #经办人查询条件
    linkmanName_text_loc = (By.NAME, "linkmanName")
    result_button_loc = (By.XPATH, "//span[contains(text(),'选择结果列')]") #选择结果列
    allResult_button_loc = (By.XPATH, "//form[@id='selectRequest']/div[7]/div/div[3]/input")
    moveRResult_button_loc = (By.XPATH, "//form[@id='selectRequest']/div[7]/div/div[3]/input[2]")
    move_button_loc = (By.ID, "moveBatchReqBC") #业务中心-迁移全部
    moveSelected_button_loc = (By.ID, "moveSelectedReqBC") #业务中心-迁移选中
    dataMove_button_loc = (By.XPATH, "//span[contains(text(),'数据迁移')]") #数据迁移
    bc_text_loc = (By.ID, "moveBusinessCenterTo-inputEl")
    moveProj_radio_loc = (By.ID, "movePrjtRadio") #项目迁移
    moveProj_text_loc = (By.ID, "moveProjectTo-inputEl")
    moveTemp_text_loc = (By.ID, "moveTemplateTo-inputEl")
    moveBC_text_loc = (By.ID, "moveBusinessCenterTo1-inputEl")
    moveProj_button_loc = (By.ID, "moveBatchReqPjt") #项目迁移-迁移全部
    moveProjSubmit_button_loc = (By.ID, "moveReqToPjtDialog_confirm")
    submit_button_loc = (By.ID, "moveReqToBCDialog_confirm")

    search_button_loc = (By.ID, "selectRequestSubmitBtn")
    exportExcel_button_loc = (By.XPATH, "//input[@value='导出excel']")
    downloadExcel_button_loc = (By.XPATH, "//a[contains(text(),'下载')]")
    selectReq_button_loc = (By.ID, "selectReqCheckbox")
    more_button_loc = (By.LINK_TEXT, '详细')
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def search_frame_in(self):
        self.iframe_in(self.search_frame_loc)

    def search_frame_out(self):
        self.iframe_out()    
 
    def searchBusiness_button(self):
        self.element(*self.searchBusiness_button_loc).click()   

    def parentBC_text(self, text):
        self.send_keys(*self.parentBC_text_loc, text=text)

    def project_text(self, text):
        self.send_keys(*self.project_text_loc, text=text)

    def template_text(self, text):
        self.send_keys(*self.template_text_loc, text=text)

    def searchCert_button(self):
        self.element(*self.searchCert_button_loc).click()

    def certType_select(self, text):
        self.select(*self.certType_select_loc, text=text)

    def searchUser_button(self):
        self.element(*self.searchUser_button_loc).click()

    def userName_text(self, text):
        self.element(*self.userName_text_loc).send_keys(text) 

    def searchLinkman_button(self):
        self.element(*self.searchLinkman_button_loc).click()  

    def linkmanName_text(self, text):
        self.element(*self.linkmanName_text_loc).send_keys(text) 

    def result_button(self):
        self.element(*self.result_button_loc).click() 

    def allResult_button(self):
        self.element(*self.allResult_button_loc).click() 

    def moveRResult_button(self):
        self.element(*self.moveRResult_button_loc).click() 

    def move_button(self):
        self.element(*self.move_button_loc).click()


    def moveSelected_button(self):
        self.element(*self.moveSelected_button_loc).click()

    def dataMove_button(self):
        self.element(*self.dataMove_button_loc).click()

    def bc_text(self, text):
        self.element(*self.bc_text_loc).send_keys(text)

    def search_button(self):
        self.element(*self.search_button_loc).click()

    def exportExcel_button(self):
        self.element(*self.exportExcel_button_loc).click()

    def downloadExcel_button(self):
        self.element(*self.downloadExcel_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def selectReq_button(self):
        self.element(*self.selectReq_button_loc).click()

    def more_button(self):
        self.element(*self.more_button_loc).click()
    
    def close_button(self):
        self.element(*self.close_button_loc).click()

    def moveProj_button(self):
        self.element(*self.moveProj_button_loc).click()

    def moveProj_text(self, text):
        self.element(*self.moveProj_text_loc).send_keys(text)

    def moveTemp_text(self, text):
        self.element(*self.moveTemp_text_loc).send_keys(text)

    def moveBC_text(self, text):
        self.element(*self.moveBC_text_loc).send_keys(text)

    def moveProj_radio(self):
        self.element(*self.moveProj_radio_loc).click()

    def moveProjSubmit_button(self):
        self.element(*self.moveProjSubmit_button_loc).click()