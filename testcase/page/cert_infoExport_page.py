from selenium.webdriver.common.by import By
from .base_page import BasePage

#导出业务登记信息
class InfoExportPage(BasePage):
    
    InfoExp_frame_loc = 2
    project_text_loc = (By.ID, "projectId-inputEl") #项目名称
    export_button_loc = (By.ID, "export") #导出
    downloadExcel_button_loc = (By.XPATH, "//a[contains(text(),'下载')]")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def InfoExp_frame_in(self):
        self.iframe_in(self.InfoExp_frame_loc)

    def InfoExp_frame_out(self):
        self.iframe_out()    
 
    def project_text(self, text): 
        self.send_keys(*self.project_text_loc, text=text)

    def export_button(self):
        self.element(*self.export_button_loc).click() #这样点击程序会一直卡在这里
        #js="document.getElementById('export').click()" 
        #self.driver.execute_script(js)

    def downloadExcel_button(self):
        temp = self.element(*self.downloadExcel_button_loc).get_attribute('href')#直接点下载没反应
        self.driver.get(temp)

    def close_button(self):
        self.element(*self.close_button_loc).click()