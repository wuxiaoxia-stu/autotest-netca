from base import Base
from selenium import webdriver
from common.screenshot import screenshot
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.user_orgUnionPay_page import OrgUnionPayPage
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_usercheck_page import UserCheckPage
from page.cert_invoice_page import InvoicePage

#用例：云南单位用户自助（如59，https://192.168.0.59/yunnan_org）
#业务信息：手机号登录申请流程，电子发票、网证通支付、定期结算。上传2个附件。
class YunnanCase(Base):

    url = Base.ip + "/yunnan_org"

    def setUp(self):
        self.test = 0
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.orgunionpaypage = OrgUnionPayPage(self.driver)


    def test_yunnan(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("云南"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.userloginpage.loginUser(self.data_org)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.upfilepage.Upfile(win=Base.win)
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payByNetca_button()
        self.paypage.chooseElectronicInvoice(self.data_org)
        oldwindow = self.paypage.orgUnionPay()
        self.orgunionpaypage.pay(oldwindow,Base.ip)
        if Base.win == '10':
            self.driver.quit()
        else:
            self.paypage.finishPay(oldwindow)
        return business_number

    def CertbpmsOper1(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.checkBusiness(business_number)
        self.checkpage.checkBusiness(False)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newEInvoice()
        self.checkpage.iframe_out()
        self.menupage.deleteCert()
