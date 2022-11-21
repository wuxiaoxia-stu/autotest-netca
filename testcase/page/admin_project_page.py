
from selenium.webdriver.common.by import By
from .base_page import BasePage

#项目添加页面
class ProjectPage(BasePage):

    project_iframe_loc = 2
    addProject_button_loc = (By.CLASS_NAME, 'add')
    projectName_text_loc = (By.ID, "name")
    projectNo_text_loc = (By.ID, "projectNumber")
    parentBusinseeCenterName_select_loc = (By.ID, "select1")
    move_button_loc = (By.XPATH, "//input[@value='＞＞']")
    submit_button_loc = (By.XPATH, "//input[@value='完成']")
    close_button_loc = (By.CLASS_NAME, 'x-tab-close-btn')

    def project_iframe_in(self):
        self.iframe_in(self.project_iframe_loc)

    def project_iframe_out(self):
        self.iframe_out()

    def addProject_button(self):
        self.element(*self.addProject_button_loc).click()

    def projectName_text(self, text):
        self.element(*self.projectName_text_loc).send_keys(text)

    def projectNo_text(self, text):
        self.element(*self.projectNo_text_loc).send_keys(text)

    def parentBusinseeCenterName_select(self, text):
        self.select(*self.parentBusinseeCenterName_select_loc, text=text)

    def move_button(self):
        self.element(*self.move_button_loc).click()

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def close_button(self):
        self.element(*self.close_button_loc).click()