from base import Base
from common.screenshot import screenshot
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_check_page import CheckPage
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.cert_usercheck_page import UserCheckPage

#用例：公诚项目单位用户自助（如59，https://192.168.0.59/gongcheng_org）
#业务信息：自助新申请时手机+验证码登录，根据申请的证件号判重
class GongchengCase(Base):

    url = Base.ip + "/gongcheng_org"
    certinfo = ["da测试项目","自动化测试-12RSA2048单位","广州班禾生物技术有限公司"]

    def setUp(self):
        self.test = 0
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)

    #验证公诚判重
    def test_gongcheng(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        self.text = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("公诚"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    #验证公诚判重
    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.userloginpage.loginUser(self.data_org)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        #已经完成申请
        self.userinfopage.identityNum_text("alreadyapply")
        self.userinfopage.next_button()
        self.assertTrue(self.userinfopage.alert() == "每个单位只能办理一个免费的公诚管理测试项目数字证书。您已经成功办理了一个，不能再次申请。")
        #用其他手机号提交申请
        self.userinfopage.identityNum_text("otherphonenumber")
        self.userinfopage.next_button()
        self.assertTrue(self.userinfopage.alert() == "每个单位只能办理一个免费的公诚管理测试项目数字证书。您已经提交了申请，不能重复提交。")
        #用自己手机号提交申请
        self.userinfopage.identityNum_text(self.now)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        #判重用自己手机号申请
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now, self.data_org)
        self.userinfopage.next_button()
        self.assertTrue(self.userinfopage.alert() == "每个单位只能办理一个免费的公诚管理测试项目数字证书，您之前已经成功提交了一份申请。是否撤销原先的申请，重新提交？")
        self.assertTrue(self.userinfopage.alert() == "撤销业务成功")
        self.userinfopage.imgValidCode_text()
        self.userinfopage.submit_button()
        self.userinfopage.alert()
        self.userinfopage.alert()
        #正常后续业务
        business_number = self.upfilepage.Upfile()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payOnDelivery_button()
        self.paypage.normalInvoice_button()
        self.paypage.payCash()
        return business_number

    def CertbpmsOper1(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.checkBusiness(business_number)
        self.checkpage.checkBusiness(False)
        self.checkpage.iframe_out()
        self.menupage.deleteCert()