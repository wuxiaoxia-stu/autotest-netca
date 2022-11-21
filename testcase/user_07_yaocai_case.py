from base import Base
from common.screenshot import screenshot
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.cert_usercheck_page import UserCheckPage
from page.cert_invoice_page import InvoicePage
from page.cert_seal_page import SealPage

#用例：药采项目单位用户自助（如59，https://192.168.0.59/yaocai）
#业务信息：自助新申请时手机+验证码登录，对附件签名，写入电子印章，印章图片查看
class YaocaiCase(Base):

    url = Base.ip + "/yaocai"
    certinfo = ["da测试项目","自动化测试-12RSA2048单位","广州班禾生物技术有限公司"]

    def setUp(self):
        self.test = 0
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.businesspage = BusinessPage(self.driver)
        self.infopage = InfoPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)
        self.sealpage = SealPage(self.driver)

    def test_yaocai(self):
        self.CertbpmsOper1()
        business_number = self.userOper1()
        self.CertbpmsOper2(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("药采"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def CertbpmsOper1(self):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.businesspage.business_frame_in()
        self.businesspage.acceptBusiness("证书申请")
        self.infopage.addInfo(self.certinfo[0],self.certinfo[1],self.certinfo[2])
        self.infopage.submit_button()
        self.checkpage.checkBusiness(False)
        self.checkresultpage.continue_button()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.userloginpage.loginUser(self.data_org)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        self.userinfopage.sealName_text("印章" + self.now)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.upfilepage.Upfile(Sign='1')
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payOnDelivery_button()
        self.paypage.chooseElectronicInvoice(self.data_org)
        self.paypage.payCash()
        return business_number

    def CertbpmsOper2(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, str(int(Base.n)+1), Base.password)
        self.menupage.deleteCert()
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.checkBusiness(business_number)
        self.checkpage.reqIDInfo_text()
        self.checkpage.exe('upload_type2.exe 7 seal.jpg 0')
        self.checkpage.signResult_text()
        self.checkpage.checkBusiness(False,True)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newEInvoice()
        self.checkresultpage.continue_button()
        self.sealpage.seal_button()
        self.sealpage.deleteSeal()
        self.checkpage.iframe_out()
        self.menupage.deleteCert()