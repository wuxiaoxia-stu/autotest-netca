import random
from base import Base
from common.screenshot import screenshot
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.user_incomplete_page import IncompletePage
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_usercheck_page import UserCheckPage
from page.cert_invoice_page import InvoicePage

#用例：多员工自助（如59，https://192.168.0.59/multistaff）

class MultiStaffCase(Base):

    url = Base.ip + "/multistaff"

    def setUp(self):
        self.test = 0
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.incompletepage = IncompletePage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.usercheckpage = UserCheckPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)

    def test_multistaff(self):
        batch_number = self.userOper1()
        self.CertbpmsOper1(batch_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("多员工"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeMultiStaffInfo(self.data_staff)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        batch_number = self.upfilepage.UpfileMultistaffs()
        business_number = self.upfilepage.reqid1_text()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.assertTrue(self.paypage.fee_text().startswith("20"))
        self.homepage.incomplete_button()
        self.userloginpage.loginUser(self.data_org)
        self.incompletepage.addUser(business_number)
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.addUserinfo(self.data_staff)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        self.upfilepage.Upfile1User()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payOnDelivery_button()
        self.paypage.normalInvoice_button()
        self.assertTrue(self.paypage.fee_text().startswith("30"))
        self.paypage.payCash()
        return batch_number

    def CertbpmsOper1(self,batch_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.checkBusinessByBatchID(batch_number)
        self.checkpage.checkBusiness(False)
        self.checkresultpage.coutinueCheck_button()
        self.checkpage.checkBusiness(True)
        self.checkresultpage.coutinueCheck_button()
        self.checkpage.checkBusiness(True)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newDinge(random.randint(10000000, 99999999), '012345678010')
        self.checkpage.iframe_out()
        self.menupage.deleteCert()