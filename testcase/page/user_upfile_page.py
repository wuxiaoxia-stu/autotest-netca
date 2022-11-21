__author__ = 'qiuju'
from selenium.webdriver.common.by import By
from .base_page import BasePage
class UpfilePage(BasePage):
    closePDF_button_loc = (By.XPATH, "//div[@id='pdfDownloadDialog']//div[3]//span")
    submit_button_loc = (By.XPATH, "//input[@value='提交']")
    nextStep_button_loc = (By.XPATH,"//input[@id='nextStep']")
    reqid_text_loc = (By.XPATH,"//td[@id='reqIdShow']")
    batchid_text_loc = (By.XPATH,"//td[@id='batchIdShow']")
    file1_button_loc = (By.XPATH,"//*[@id='reqFileTable']/tbody/tr[2]/td[2]/span/div[2]")
    file2_button_loc = (By.XPATH, "//*[@id='reqFileTable']/tbody/tr[3]/td[2]/span/div[2]")
    #多业务附件
    multifile1_button_loc = (By.XPATH,"//*[@id='reqFileTable']/tbody/tr[2]/td[2]/span/div[2]") #申请表
    multifile2_button_loc = (By.XPATH,"//*[@id='reqFileTable']/tbody/tr[3]/td[2]/span/div[2]") #单位附件
    multifile3_button_loc = (By.XPATH,"//*[@id='reqFileTable']/tbody/tr[4]/td[2]/span/div[2]") #经办人附件
    stafffile1_button_loc = (By.XPATH,"//*[@id='MulReqFileTipsTable2']/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/span/div[2]") #员工1附件
    stafffile2_button_loc = (By.XPATH,"//*[@id='MulReqFileTipsTable2']/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/span/div[2]") #员工2附件
    stafffile3_button_loc = (By.XPATH,"//*[@id='MulReqFileTipsTable2']/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/span/div[2]")  # 员工3附件
    reqid1_text_loc = (By.XPATH,"//*[@id='MulReqFileTipsTable2']/tbody/tr/td")

    def closePDF_Button(self):
        self.element(*self.closePDF_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def nextStep_button(self):
        self.element(*self.nextStep_button_loc).click()

    def reqid_text(self):
        return self.text(*self.reqid_text_loc)

    def batchid_text(self):
        return self.text(*self.batchid_text_loc)

    def reqid1_text(self):
        reqtext = self.text(*self.reqid1_text_loc)
        reqid = reqtext.split("（")[2].split("）")[0]
        return reqid

    #附件上传1
    def file1_button(self):
        self.element(*self.file1_button_loc).click()

    #附件上传2
    def file2_button(self):
        self.element(*self.file2_button_loc).click()

    #多业务附件
    #申请表附件
    def multifile1_button(self):
        self.element(*self.multifile1_button_loc).click()

    #单位附件
    def multifile2_button(self):
        self.element(*self.multifile2_button_loc).click()

    #经办人附件
    def multifile3_button(self):
        self.element(*self.multifile3_button_loc).click()

    #员工1附件
    def stafffile1_button(self):
        self.element(*self.stafffile1_button_loc).click()

    #员工2附件
    def stafffile2_button(self):
        self.element(*self.stafffile2_button_loc).click()

    # 员工2附件
    def stafffile3_button(self):
        self.element(*self.stafffile3_button_loc).click()

    #关闭导出PDF，上传附件
    def Upfile(self,win='7',closePDF=True,Sign='0'):
        self.sleep(1)
        if closePDF == True:
            self.closePDF_Button()
        self.file1_button()
        self.exe('upload_type2.exe '+ win +' 3.jpg '+Sign)
        self.file2_button()
        self.exe('upload_type2.exe '+ win +' 4.jpg '+Sign)
        return self.reqid_text()

    #多业务上传附件
    def UpfileMultistaffs(self):
        self.sleep(1)
        self.closePDF_Button()
        self.multifile1_button()
        self.exe('upload_type2.exe 7 1.png 0')
        self.multifile2_button()
        self.exe('upload_type2.exe 7 3.jpg 0')
        self.multifile3_button()
        self.exe('upload_type2.exe 7 4.jpg 0')
        self.stafffile1_button()
        self.exe('upload_type2.exe 7 3.jpg 0')
        self.stafffile2_button()
        self.exe('upload_type2.exe 7 4.jpg 0')
        return self.batchid_text()

    #多业务添加第3个员工的附件
    def Upfile1User(self):
        self.sleep(1)
        self.closePDF_Button()
        self.stafffile3_button()
        self.exe('upload_type2.exe 7 1.png 0')