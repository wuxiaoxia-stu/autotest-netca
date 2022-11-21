from base import Base
from common.screenshot import screenshot
from page.user_pingan_page import PinganPage
from page.user_home_page import HomePage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_usercheck_page import UserCheckPage
from page.cert_invoice_page import InvoicePage
from page.cert_seal_page import SealPage

#用例：平安跳转页面（http://192.168.0.127:8080/thirdpartAuth/createTicket.jsp）
#用例1：新申请完整流程、平安第三方跳转新申请流程，电子发票、网证通支付、企业银联。上传2个附件。
class PinganCase(Base):

    url = "http://192.168.0.127:8080/thirdpartAuth/createTicket.jsp"

    def setUp(self):
        self.test = 0
        self.pinganpage = PinganPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)
        self.sealpage = SealPage(self.driver)

    def test_pingan(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        self.userOper2()
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("平安"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.pinganpage.open(self.url)
        self.pinganpage.apply(self.now,self.now)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        self.userinfopage.sealName_text("印章"+self.now)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.upfilepage.Upfile()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payByNetca_button()
        self.paypage.chooseElectronicInvoice(self.data_org)
        self.paypage.payCash()
        return business_number

    def CertbpmsOper1(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
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
        self.sealpage.iframe_out()
        self.menupage.deleteCert()

    def userOper2(self):
        self.pinganpage.open(self.url)
        self.pinganpage.apply(self.now,self.now)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.assertTrue("请勿重复" in self.userinfopage.pingAn_text())