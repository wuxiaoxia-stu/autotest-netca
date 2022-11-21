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
from page.cert_seal_page import SealPage

#用例：辽宁政采项目用户自助（如59，https://192.168.0.59/lnzc）
#业务信息：辽宁政采页面指向用户自助。
class LiaoningCase(Base):

    url = Base.ip + "/lnzc"

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
        self.sealpage = SealPage(self.driver)

    def test_liaoning(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        business_number = self.userOper1(promoCode=True)
        self.CertbpmsOper1(business_number=business_number,checkpromoCode=True)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("辽宁政采"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self,promoCode=False):
        self.homepage.open(self.url)
        if promoCode:
            newurl = self.homepage.getURL()+"&promoCode="+self.now
            self.homepage.open(newurl)
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeStaffInfo(self.now,self.data_staff)
        self.userinfopage.validity_select("12")
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.upfilepage.Upfile()
        self.upfilepage.sleep(5)
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payByBusiness_Button()
        self.paypage.chooseVatInvoice()
        self.paypage.payCash()
        return business_number


    def CertbpmsOper1(self,business_number,checkpromoCode=False):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.reqID_text(business_number)
        self.usercheckpage.search_button()
        self.usercheckpage.detail_button()
        if checkpromoCode:
            self.assertTrue(self.usercheckpage.promoCode_text()==(self.now))
        else :
            self.assertTrue(self.usercheckpage.promoCode_text() == (""))
        self.usercheckpage.submit_button()
        self.usercheckpage.goCheck_button()
        if checkpromoCode:
            self.assertTrue(self.checkpage.promoCode_text()==(self.now))
        else :
            self.assertTrue(self.checkpage.promoCode_text() == (""))
        self.checkpage.checkBusiness(False)
        self.checkpage.alert()
        self.checkpage.check_button()
        self.checkpage.searchBusiness(business_number)
        self.checkpage.detail_button()
        if checkpromoCode:
            self.assertTrue(self.checkpage.promoCode_text()==(self.now))
        else :
            self.assertTrue(self.checkpage.promoCode_text() == (""))
        self.checkpage.checkBusiness(False)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newZhuanpiao(random.randint(10000000, 99999999), '012345678000', 20)
        self.sealpage.iframe_out()
        self.menupage.deleteCert()



