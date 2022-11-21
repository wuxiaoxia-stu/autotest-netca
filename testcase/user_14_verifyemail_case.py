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
from common.config import read_config


#用例：校验邮箱（如59，https://192.168.0.59/verifyemail）
#业务信息：普通申请流程，上传2个附件,普通发票，现金支付。获取邮件确认邮箱
class CheckemailCase(Base):

    url = Base.ip + "/verifyemail"

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

    def test_verifyemail(self):
        business_number = self.userOper1()
        self.CertbpmsOper1(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("校验邮箱"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        self.userinfopage.email_textinput(read_config('getemail', 'email'))
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        self.userinfopage.closeEmail_button()
        business_number = self.upfilepage.Upfile()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payOnDelivery_button()
        self.paypage.normalInvoice_button()
        self.paypage.payCash()
        self.assertTrue(self.homepage.verifyEmail().startswith("恭喜您，您已经验证成功！"))
        return business_number

    def CertbpmsOper1(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.usercheckpage.check_frame_in()
        self.usercheckpage.check_button()
        self.usercheckpage.reqID_text(business_number)
        self.usercheckpage.search_button()
        self.usercheckpage.detail_button()
        self.usercheckpage.verify_button()
        self.assertTrue(self.userinfopage.alert().startswith("发送失败"))
        self.usercheckpage.getResult_button()
        self.assertTrue(self.usercheckpage.result_text().startswith("用户已验证"))
        self.usercheckpage.submit_button()
        self.usercheckpage.goCheck_button()
        self.checkpage.checkBusiness(False)
        self.checkresultpage.newInvoice_button()
        self.invoicepage.newDinge(random.randint(10000000, 99999999), '012345678010')
        self.checkpage.iframe_out()
        self.menupage.deleteCert()