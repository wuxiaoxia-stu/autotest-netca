import random
from base import Base
from common.screenshot import screenshot
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

#用例：普通个人用户自助（如59，https://192.168.0.59/tongyong_per）
#业务信息：普通申请流程，普通发票、快递到付、现金支付。上传2个附件。
class PerCase(Base):

    url = Base.ip + "/tongyong_per"

    def setUp(self):
        self.test = 0
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

    def test_tongyongper(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("通用个人"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writePerInfo(self.data_per)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
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
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newDinge(random.randint(10000000, 99999999), '012345678010')
        self.checkpage.iframe_out()
        self.menupage.deleteCert()