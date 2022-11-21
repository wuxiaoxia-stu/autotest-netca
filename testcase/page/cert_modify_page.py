
from selenium.webdriver.common.by import By
from .base_page import BasePage

#业务信息
class ModifyPage(BasePage):  
   
    changeCA_button_loc = (By.XPATH, "//div[@id='isChangeCADiv']/div[2]/input[2]")
    project_text_loc = (By.ID, "projectId-inputEl")
    template_text_loc = (By.ID, "templateId-inputEl")
    identityType_select_loc = (By.ID, "identityType")
    identity_text_loc = (By.ID, "identityShow")
    userName_text_loc = (By.ID, "userNameShow")
    countryName_select_loc = (By.ID, "countryName")
    province_select_loc = (By.ID, "province")
    city_select_loc = (By.ID, "city")
    phone_text_loc = (By.ID, "phoneShow")
    email_text_loc = (By.ID, "emailShow")
    department_text_loc = (By.ID, "departmentShow")   
    residence_text_loc = (By.ID, "officialResidenceShow")
    type_select_loc = (By.ID, "organizationType")

    lIdentityType_select_loc = (By.ID, "linkmanIdentityType")
    lIdentity_text_loc = (By.ID, "linkmanIdentityShow")
    lName_text_loc = (By.ID, "linkmanNameShow")
    lPhone_text_loc = (By.ID, "linkmanPhoneShow")
    lEmail_text_loc = (By.ID, "linkmanEmailShow")

    oIdentityType_select_loc = (By.ID, "orgidentityType")
    oIdentity_text_loc = (By.ID, "orgidentityShow")
    oUserName_text_loc = (By.ID, "orguserNameShow")
    oCountryName_select_loc = (By.ID, "orgcountryName")
    oProvince_select_loc = (By.ID, "orgprovince")
    oPhone_text_loc = (By.ID, "orgphoneShow")
    oResidence_text_loc = (By.ID, "orgofficialResidenceShow")
    oType_select_loc = (By.ID, "organizationType")

    addFile_button_loc = (By.ID, "addRequestFile")
    upload_button_loc = (By.ID, "SWFUpload_0")
    getGeren_button_loc = (By.ID, "getLinkManInfoByUserInfoBtn")
    getDanwei_button_loc = (By.ID, "getLinkmanByIdBtn")
    getYuangong_button_loc = (By.ID, "getLatestLinkmanByOrgIdBtn")
    submit_button_loc = (By.XPATH, "//input[@value='提交']")
    submitModify_button_loc = (By.XPATH, "//input[@value='修改']")
    check_button_loc = (By.LINK_TEXT, "审核")
    tipModify_text_loc = (By.XPATH, "//div[@id='getRequestByIdDialogBox']/div/div")

    # 申请印章
    isNeedSeal_button_loc = (By.XPATH, "//input[@id='isNeedSealReq']")

    def project_text(self, text): 
        self.send_keys(*self.project_text_loc, text=text)

    def template_text(self, text):
        self.send_keys(*self.template_text_loc, text=text)

    def identityType_select(self, text):
        self.select(*self.identityType_select_loc, text=text)

    def identity_text(self, text):
        self.input(*self.identity_text_loc, text=text)

    def userName_text(self, text):
        self.input(*self.userName_text_loc, text=text)

    def countryName_select(self, text):
        self.select(*self.countryName_select_loc, text=text)

    def province_select(self, text):
        self.select(*self.province_select_loc, text=text)

    def city_select(self, text):
        self.select(*self.city_select_loc, text=text)

    def phone_text(self, text):
        self.input(*self.phone_text_loc, text=text)

    def email_text(self, text):
        self.input(*self.email_text_loc, text=text)

    def department_text(self, text):
        self.input(*self.department_text_loc, text=text)

    def residence_text(self, text):
        self.input(*self.residence_text_loc, text=text)

    def type_select(self, text):
        self.select(*self.type_select_loc, text=text)

    def lIdentityType_select(self, text):
        self.select(*self.lIdentityType_select_loc, text=text)

    def lIdentity_text(self, text):
        self.input(*self.lIdentity_text_loc, text=text)

    def lName_text(self, text):
        self.input(*self.lName_text_loc, text=text)

    def lPhone_text(self, text):
        self.input(*self.lPhone_text_loc, text=text)

    def lEmail_text(self, text):
        self.input(*self.lEmail_text_loc, text=text)  

    def oIdentityType_select(self, text):
        self.select(*self.oIdentityType_select_loc, text=text)

    def oIdentity_text(self, text):
        self.input(*self.oIdentity_text_loc, text=text)  

    def oUserName_text(self, text):
        self.input(*self.oUserName_text_loc, text=text)  

    def oCountryName_text(self, text):
        self.select(*self.oCountryName_select_loc, text=text)

    def oProvince_text(self, text):
        self.select(*self.oProvince_select_loc, text=text)  

    def oPhone_text(self, text):
        self.input(*self.oPhone_text_loc, text=text) 

    def oResidence_text(self, text):
        self.input(*self.oResidence_text_loc, text=text) 

    def oType_text(self, text):
        self.select(*self.oType_select_loc, text=text)  

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def getGeren_button(self):
        self.element(*self.getGeren_button_loc).click()  

    def getDanwei_button(self):
        self.element(*self.getDanwei_button_loc).click() 

    def getYuangong_button(self):
        self.element(*self.getYuangong_button_loc).send_keys(' ')
        #self.element(*self.getYuangong_button_loc).click()

    def addFile_button(self):
        self.element(*self.addFile_button_loc).click() 

    def upload_button(self):
        self.element(*self.upload_button_loc).click() 

    def submitModify_button(self):
        self.element(*self.submitModify_button_loc).click()

    def check_button(self):
        self.element(*self.check_button_loc).click()

    def changeCA_button(self):
        self.element(*self.changeCA_button_loc).click()

    def isNeedSeal_button(self):
        self.element(*self.isNeedSeal_button_loc).click()

    def tipModify_text(self):
        return self.text(*self.tipModify_text_loc) 

    def addInfo(self, project, template, userName):
        """
        输入：项目、模板、用户名称
        操作：选择项目、模板后，录入用户信息
        """
        self.project_text(project)
        self.template_text(template)

        self.identityType_select('1')
        self.identity_text('236504195106192666')
        self.userName_text(userName)
        self.countryName_select('中国')
        self.province_select('广东')
        self.city_select('广州')
        self.phone_text('0123')
        self.email_text('zs@cnca.net')
        self.department_text('测试部门')
        self.residence_text('测试地址')
        self.type_select('1')
        
        self.oIdentityType_select('1')
        self.oIdentity_text('91371321MA3D54FM8C')
        self.oUserName_text('测试单位')
        self.oCountryName_text('中国')
        self.oProvince_text('广东')
        self.oPhone_text('020-38861610')
        self.oResidence_text('测试地址')
        self.oType_text('1')

        self.lIdentityType_select('1')
        self.lIdentity_text('236504195106192666')
        self.lName_text('经办人')
        self.lPhone_text('0123')
        self.lEmail_text('zs@cnca.net')

