from base import Base
from common.screenshot import screenshot
from common import TraverseDevice
from common import KeyRegedit
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.user_home_page import HomePage
from page.user_protocol_page import ProtocolPage
from page.user_serviceInformation_page import ServiceInformationPage
from page.user_info_page import UserInfoPage
from page.user_pay_page import PayPage
from page.user_apply_page import ApplyPage


class UserApplyCase(Base):

    url = Base.ip + "/userapply"
    keynum = TraverseDevice.GetDeviceNum()
    certinfo = ["da测试项目", "自动化测试-12RSA2048单位"]

    def setUp(self):
        self.test = 0
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.businesspage = BusinessPage(self.driver)
        self.infopage = InfoPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.serviceinformationPage = ServiceInformationPage(self.driver)
        self.userinfopage = UserInfoPage(self.driver)
        self.paypage = PayPage(self.driver)
        self.applypage = ApplyPage(self.driver)

    def test_userapply(self):
        self.CertbpmsOper1()
        business_number = self.userOper1()
        self.CertbpmsOper2(business_number)
        self.userOper2()
        self.CertbpmsOper3()
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("应用开通"+nowTime)#用例脚本运行报错立刻截图保存
            KeyRegedit.ChangeRegedit(self.keynum, "put")
        #self.driver.close()

    def CertbpmsOper1(self):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.businesspage.business_frame_in()
        self.businesspage.acceptBusiness("证书申请")
        self.infopage.addInfo(self.certinfo[0], self.certinfo[1], self.data_org[3])
        self.infopage.submit_button()
        self.checkpage.checkBusiness(False)
        self.checkresultpage.continue_button()

    def userOper1(self):
        KeyRegedit.ChangeRegedit(self.keynum, "pull")
        self.homepage.open(self.url)
        self.homepage.application_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.assertTrue(self.applypage.Selectapply_Text().startswith("警告：应用的结束时间："))
        self.userinfopage.writeLinkmanInfo(self.data_org)
        self.userinfopage.applySubmit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.paypage.businessNumber_text()
        self.paypage.chooseElectronicInvoice(self.data_org)
        self.paypage.payCash()
        KeyRegedit.ChangeRegedit(self.keynum, "put")
        return business_number



    def CertbpmsOper2(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, str(int(Base.n) + 1), Base.password)
        self.menupage.business_button()
        self.checkpage.check_frame_in()
        self.checkpage.check_button()
        self.checkpage.searchBusiness(business_number)
        self.checkpage.detail_button()
        self.checkpage.submit_button()
        self.checkresultpage.continue_button()

    def userOper2(self):
        KeyRegedit.ChangeRegedit(self.keynum, "pull")
        self.homepage.open(self.url)
        self.homepage.application_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.assertTrue(self.applypage.alert().startswith("该证书已经开通过应用："))
        KeyRegedit.ChangeRegedit(self.keynum, "put")

    def CertbpmsOper3(self):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, str(int(Base.n) + 1), Base.password)
        self.menupage.deleteCert()

