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
from page.user_perUnionPay_page import PerUnionPayPage
from page.cert_usercheck_page import UserCheckPage
from page.cert_invoice_page import InvoicePage


#用例：耗材项目单位用户自助（如59，https://192.168.0.59/haocai）
#业务信息：授权人登录申请流程，电子发票、用户到付、个人银联支付。上传2个附件（上传需要签名）。
class HaocaiCase(Base):

    url = Base.ip + "/haocai"
    certinfo = ["da测试项目","自动化测试-12RSA2048单位","耗材自动化测试单位名"]
    haocaiinfo = ["耗材自动化测试单位名","经办人"]

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
        self.perunionpaypage = PerUnionPayPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)

    def test_haocai(self):
        self.CertbpmsOper1()
        business_number = self.userOper1()
        self.CertbpmsOper2(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("耗材"+nowTime)#用例脚本运行报错立刻截图保存
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
        self.userloginpage.loginHaoCai(self.haocaiinfo[0],self.haocaiinfo[1],self.data_org[12])
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
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
        self.checkpage.checkBusiness(False)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newEInvoice()
        self.checkpage.iframe_out()
        self.menupage.deleteCert()