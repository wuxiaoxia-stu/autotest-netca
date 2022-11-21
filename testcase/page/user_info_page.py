__author__ = 'qiuju'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

#用户信息填写页面
class UserInfoPage(BasePage):
    validity_select_loc = (By.ID, 'month')
    identityType_select_loc = (By.ID, 'identityType')
    identityType_select_loc1 = (By.ID, 'selfServiceUsers_0_identityType')
    identityType_select_loc2 = (By.ID, 'selfServiceUsers_1_identityType')
    orgIdentityType_select_loc = (By.ID, 'orgidentityType')
    identityNum_text_loc = (By.ID, 'identityShow')
    identityNum_text_loc1 = (By.ID, 'selfServiceUsers_0_identityShow')
    identityNum_text_loc2 = (By.ID, 'selfServiceUsers_1_identityShow')
    orgIdentityNum_text_loc = (By.ID, 'orgidentityShow')
    orgUserName_text_loc = (By.ID, 'orguserNameShow')
    userName_text_loc = (By.ID, 'userNameShow')
    userName_text_loc1 = (By.ID, 'selfServiceUsers_0_userNameShow')
    userName_text_loc2 = (By.ID, 'selfServiceUsers_1_userNameShow')
    province_select_loc = (By.ID, 'province')
    province_select_loc1 = (By.ID, 'selfServiceUsers_0_province')
    province_select_loc2 = (By.ID, 'selfServiceUsers_1_province')
    city_select_loc = (By.ID, 'city')
    phone_text_loc = (By.ID, 'phoneShow')
    orgPhone_text_loc = (By.ID, 'orgphoneShow')
    orgLegalAddress_text_loc = (By.XPATH, "//textarea[@id='orgofficialResidenceShow']")
    legalAddress_text_loc = (By.XPATH, "//textarea[@id='officialResidenceShow']")
    yunNanNum_text_loc = (By.XPATH,"//input[@title='云南电力交易系统账号']")
    orgCommunicateAddress_text_loc = (By.XPATH, "//textarea[@id='orgaddressShow']")
    communicateAddress_text_loc = (By.ID, "addressShow")
    communicateAddress_text_loc1 = (By.ID, "selfServiceUsers_0_officialResidenceShow")
    communicateAddress_text_loc2 = (By.ID, "selfServiceUsers_1_officialResidenceShow")
    email_text_loc = (By.ID, 'emailShow')
    email_text_loc1 = (By.ID, 'selfServiceUsers_0_emailShow')
    email_text_loc2 = (By.ID, 'selfServiceUsers_1_emailShow')
    department_text_loc = (By.ID, 'departmentShow')
    department_text_loc1 = (By.ID, 'selfServiceUsers_0_departmentShow')
    department_text_loc2 = (By.ID, 'selfServiceUsers_1_departmentShow')
    yunNanID_text_loc = (By.XPATH, "//input[@title='云南电力交易系统用户ID']")
    fax_text_loc = (By.XPATH, "//input[@title='传真']")
    gzdlNum_text_loc = (By.XPATH, "//input[@title='贵州电力市场交易系统账号']")
    certSource_text_loc = (By.XPATH, "//input[@title='证书来源']")
    postcode_text_loc = (By.XPATH, "//input[@title='邮政编码']")
    businessLicenseNum_text_loc = (By.XPATH, "//input[@title='营业执照注册号(企业)']")
    area_select_loc = (By.ID, 'area')
    pingAnYinZhang_text_loc = (By.XPATH,"//*[@id='sealApplyObjectTable']/tbody/tr[2]/td[2]/input")
    #香港序列号
    hkSerialNumber_text_loc = (By.XPATH,"//input[@title='香港序列号']")

    #经办人信息字段
    linkmanIdentityType_select_loc = (By.ID, 'linkmanIdentityType')
    linkmanIdentityNum_text_loc = (By.ID, 'linkmanIdentityShow')
    linkmanName_text_loc = (By.ID, 'linkmanNameShow')
    linkmanPhone_text_loc = (By.ID, 'linkmanPhoneShow')
    linkmanEmail_text_loc = (By.ID, 'linkmanEmailShow')
    linkmanAddress_text_loc = (By.XPATH, "//textarea[@id='linkmanAddressShow']")
    #备注信息
    memo_text_loc = (By.XPATH, "//textarea[@id='memo']")

    addUser_button_loc = (By.ID, 'combinedReqAddUserBtn')
    getFromUser_button_loc = (By.XPATH, "//input[@value='从用户信息获取']")

    next_button_loc = (By.XPATH,"//input[@id='nextButton']")
    imgValidCode_text_loc = (By.XPATH,"//input[@id='imgValidCodeText']")
    back_button_loc = (By.XPATH, "//input[@value='返 回']")
    submit_button_loc = (By.XPATH,"//input[@value='提 交']")

    #应用开通页面的填写信息 下一步按钮（没有id属性）
    applyNext_button_loc = (By.XPATH,"//input[@value='下一步' and @class='button']")
    applySubmit_button_loc = (By.XPATH, "//input[@value='提 交']")

    #印章名称
    sealName_text_loc = (By.XPATH,"//input[@title='印章名称']")

    #关闭验证邮箱弹窗
    closeEmail_button_loc = (By.XPATH,"//span[@id='emailTipsDialog_titleClose']")

    #平安新申请判重
    pingAn_text_loc = (By.XPATH,"//*[@id='comfirmDialogBox']/div/div")

    def sealName_text(self,text):
        #self.input(*self.sealName_text_loc, text=text)
        js = "document.getElementById('sealName').setAttribute('value','" + text + "')"
        self.driver.execute_script(js)

    def closeEmail_button(self):
        self.element(*self.closeEmail_button_loc).click()

    def validity_select(self, text):
        self.select(*self.validity_select_loc, text=text)

    def identityType_select(self, text):
        self.select(*self.identityType_select_loc, text=text)

    def identityType_select1(self, text):
        self.select(*self.identityType_select_loc1, text=text)

    def identityType_select2(self, text):
        self.select(*self.identityType_select_loc2, text=text)

    def orgIdentityType_select(self, text):
        self.select(*self.orgIdentityType_select_loc, text=text)

    def identityNum_text(self, text):
        self.input(*self.identityNum_text_loc, text=text)

    def identityNum_text1(self, text):
        self.input(*self.identityNum_text_loc1, text=text)

    def identityNum_text2(self, text):
        self.input(*self.identityNum_text_loc2, text=text)

    def orgIdentityNum_text(self, text):
        self.input(*self.orgIdentityNum_text_loc, text=text)

    def orgUserName_text(self, text):
        self.input(*self.orgUserName_text_loc, text=text)

    def userName_text(self, text):
        self.input(*self.userName_text_loc, text=text)

    def userName_text1(self, text):
        self.input(*self.userName_text_loc1, text=text)

    def userName_text2(self, text):
        self.input(*self.userName_text_loc2, text=text)

    def province_select(self, text):
        self.select(*self.province_select_loc, text=text)

    def province_select1(self, text):
        self.select(*self.province_select_loc1, text=text)

    def province_select2(self, text):
        self.select(*self.province_select_loc2, text=text)

    def city_select(self, text):
        self.select(*self.city_select_loc, text=text)

    def phone_text(self, text):
        self.input(*self.phone_text_loc, text=text)

    def orgPhone_text(self, text):
        self.input(*self.orgPhone_text_loc, text=text)

    def orgLegalAddress_text(self, text):
        self.input(*self.orgLegalAddress_text_loc, text=text)

    def legalAddress_text(self, text):
        self.input(*self.legalAddress_text_loc, text=text)

    def yunNanNum_text(self, text):
        self.input(*self.yunNanNum_text_loc, text=text)

    def orgCommunicateAddress_text(self, text):
        self.input(*self.orgCommunicateAddress_text_loc, text=text)

    def communicateAddress_text(self, text):
        self.input(*self.communicateAddress_text_loc, text=text)

    def communicateAddress_text1(self, text):
        self.input(*self.communicateAddress_text_loc1, text=text)

    def communicateAddress_text2(self, text):
        self.input(*self.communicateAddress_text_loc2, text=text)

    def email_text(self, text):
        #self.input(*self.email_text_loc, text=text)
        email = text.split('@')[0]+'@'
        try:
            self.driver.find_element_by_id("emailShow").clear()
            self.driver.find_element_by_id("emailShow").send_keys(email)
            self.driver.find_element_by_id("emailShow").send_keys(Keys.DOWN)
            self.driver.find_element_by_id("emailShow").send_keys(Keys.ENTER)
        except:
            pass

    def email_text1(self, text):
        self.input(*self.email_text_loc1, text=text)

    def email_text2(self, text):
        self.input(*self.email_text_loc2, text=text)

    def email_textinput(self,text):
        self.input(*self.email_text_loc,text=text)

    def department_text(self, text):
        self.input(*self.department_text_loc, text=text)

    def department_text1(self, text):
        self.input(*self.department_text_loc1, text=text)

    def department_text2(self, text):
        self.input(*self.department_text_loc2, text=text)

    def yunNanID_text(self, text):
        self.input(*self.yunNanID_text_loc, text=text)

    def fax_text(self, text):
        self.input(*self.fax_text_loc, text=text)

    def gzdlNum_text(self, text):
        self.input(*self.gzdlNum_text_loc, text=text)

    def certSource_text(self, text):
        self.input(*self.certSource_text_loc, text=text)

    def postCode_text(self, text):
        self.input(*self.postcode_text_loc, text=text)

    def businessLicenseNum_text(self, text):
        self.input(*self.businessLicenseNum_text_loc, text=text)

    def area_select(self, text):
        self.select(*self.area_select_loc, text=text)

    def pingAnYinZhang_text(self, text):
        self.input(*self.pingAnYinZhang_text_loc, text=text)

    def hkSerialNumber_text(self, text):
        self.input(*self.hkSerialNumber_text_loc, text=text)

    def linkmanIdentityType_select(self, text):
        self.select(*self.linkmanIdentityType_select_loc, text=text)

    def linkmanIdentityNum_text(self, text):
        self.input(*self.linkmanIdentityNum_text_loc, text=text)

    def linkmanName_text(self, text):
        self.input(*self.linkmanName_text_loc, text=text)

    def linkmanPhone_text(self, text):
        self.input(*self.linkmanPhone_text_loc, text=text)

    def linkmanEmail_text(self, text):
        self.input(*self.linkmanEmail_text_loc, text=text)

    def linkmanAddress_text(self, text):
        self.input(*self.linkmanAddress_text_loc, text=text)

    def memo_text(self, text):
        self.input(*self.memo_text_loc, text=text)

    def addUser_button(self):
        self.element(*self.addUser_button_loc).click()

    def getFromUser_button(self):
        self.element(*self.getFromUser_button_loc).click()

    def next_button(self):
        self.element(*self.next_button_loc).click()

    def applyNext_button(self):
        self.element(*self.applyNext_button_loc).click()

    def applySubmit_button(self):
        self.element(*self.applySubmit_button_loc).click()

    def imgValidCode_text(self):
        self.input(*self.imgValidCode_text_loc,text="1234")

    def submit_button(self):
        self.element(*self.submit_button_loc).click()

    def back_button(self):
        self.element(*self.back_button_loc).click()

    #尝试获取验证信息
    def pingAn_text(self):
        try:
            return self.text(*self.pingAn_text_loc)
        except:
            return None

    #写单位信息
    def writeOrgInfo(self, now,*org_value):
        self.validity_select(org_value[0][0])
        self.identityType_select(org_value[0][1])
        self.identityNum_text(now)
        self.userName_text(org_value[0][3])
        self.province_select(org_value[0][4])
        self.city_select(org_value[0][5])
        self.phone_text(org_value[0][6])
        self.legalAddress_text(org_value[0][7])
        self.yunNanNum_text(now)
        self.communicateAddress_text(org_value[0][8])
        self.linkmanIdentityType_select(org_value[0][9])
        self.linkmanIdentityNum_text(org_value[0][10])
        self.linkmanName_text(org_value[0][11])
        self.linkmanPhone_text(org_value[0][12])
        self.linkmanEmail_text(org_value[0][13])
        self.linkmanAddress_text(org_value[0][14])
        self.memo_text(org_value[0][15])
        self.email_text(org_value[0][16])
        self.postCode_text(org_value[0][17])
        self.area_select(org_value[0][18])
        self.businessLicenseNum_text(org_value[0][2])
        self.fax_text(org_value[0][6])
        self.gzdlNum_text(now)
        self.certSource_text(now)

    #员工信息(未使用)
    def writeStaffInfo(self,now,*staff_value):
        self.validity_select(staff_value[0][0])
        self.orgIdentityType_select(staff_value[0][1])
        self.orgIdentityNum_text(staff_value[0][2])
        self.orgUserName_text(staff_value[0][3])
        self.province_select(staff_value[0][4])
        self.city_select(staff_value[0][5])
        self.orgPhone_text(staff_value[0][6])
        self.orgLegalAddress_text(staff_value[0][7])
        self.yunNanNum_text(now)
        self.orgCommunicateAddress_text(staff_value[0][8])

        self.identityType_select(staff_value[0][9])
        self.identityNum_text(staff_value[0][10])
        self.userName_text(staff_value[0][11])
        self.province_select(staff_value[0][12])
        self.city_select(staff_value[0][13])
        self.department_text(staff_value[0][14])
        self.phone_text(staff_value[0][15])
        self.legalAddress_text(staff_value[0][16])
        self.yunNanNum_text(now)
        self.communicateAddress_text(staff_value[0][17])
        self.email_text('test@cnca.net')

        self.getFromUser_button()
        self.linkmanAddress_text(staff_value[0][18])
        self.linkmanEmail_text(staff_value[0][19])
        self.memo_text(staff_value[0][20])
        self.linkmanPhone_text(staff_value[0][15])
        self.certSource_text("证书来源123asdf")


    # 多业务员工信息
    def writeMultiStaffInfo(self, *staff_value):
        self.validity_select(staff_value[0][0])
        self.orgIdentityType_select(staff_value[0][1])
        self.orgIdentityNum_text(staff_value[0][2])
        self.orgUserName_text('测试单位')
        self.province_select(staff_value[0][4])
        self.city_select(staff_value[0][5])
        self.orgPhone_text('020-38861610')
        self.orgLegalAddress_text(staff_value[0][7])
        self.orgCommunicateAddress_text(staff_value[0][8])

        self.identityType_select1(staff_value[0][9])
        self.identityNum_text1(staff_value[0][10]+"11")
        self.userName_text1('多业务员工1')
        self.province_select1(staff_value[0][12])
        self.department_text1(staff_value[0][14]+"11")
        self.communicateAddress_text1(staff_value[0][17]+"11")

        self.addUser_button()
        self.identityType_select2(staff_value[0][9])
        self.identityNum_text2(staff_value[0][10]+"22")
        self.userName_text2('多业务员工2')
        self.province_select2(staff_value[0][12])
        self.department_text2(staff_value[0][14]+"22")
        self.communicateAddress_text2(staff_value[0][17]+"22")

        self.getFromUser_button()
        self.linkmanAddress_text(staff_value[0][18])
        self.linkmanEmail_text(staff_value[0][19])
        self.memo_text(staff_value[0][20])
        self.linkmanPhone_text(staff_value[0][15])

    #写个人信息
    def writePerInfo(self, *per_value):
        self.validity_select(per_value[0][0])
        self.identityType_select(per_value[0][1])
        self.identityNum_text(per_value[0][2])
        self.userName_text(per_value[0][3])
        self.province_select(per_value[0][4])
        self.city_select(per_value[0][5])
        self.department_text(per_value[0][6])
        self.phone_text(per_value[0][7])
        self.legalAddress_text(per_value[0][8])
        self.email_text(per_value[0][9])
        self.communicateAddress_text(per_value[0][10])
        self.getFromUser_button()
        self.linkmanAddress_text(per_value[0][11])
        self.memo_text(per_value[0][12])
        self.certSource_text("证书来源123asdf")
        # da测试：香港序列号
        self.hkSerialNumber_text("123")

    #写经办人信息
    def writeLinkmanInfo(self,*org_value):
        self.linkmanIdentityType_select(org_value[0][9])
        self.linkmanIdentityNum_text(org_value[0][10])
        self.linkmanName_text(org_value[0][11])
        self.linkmanPhone_text(org_value[0][12])
        self.linkmanEmail_text(org_value[0][13])
        self.linkmanAddress_text(org_value[0][14])

    def submit(self):
        self.next_button()
        self.imgValidCode_text()
        self.submit_button()

    #应用开通的下一步-验证码-提交流程
    def applySubmit(self):
        self.applyNext_button()
        self.imgValidCode_text()
        self.applySubmit_button()

    #多员工业务添加员工
    def addUserinfo(self,*staff_value):
        self.identityType_select1(staff_value[0][9])
        self.identityNum_text1(staff_value[0][10] + "33")
        self.userName_text1('多业务员工3')
        self.province_select1(staff_value[0][12])
        self.department_text1(staff_value[0][14] + "33")
        self.communicateAddress_text1(staff_value[0][17] + "33")