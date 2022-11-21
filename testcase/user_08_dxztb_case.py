from base import Base
from common.screenshot import screenshot
from page.user_org4SM2_page import Org4SM2Page
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_incomplete_page import IncompletePage
from page.user_modifyInformation_page import ModifyInformationPage
from page.user_upfile_page import UpfilePage
from page.user_pay_page import PayPage
from page.user_perUnionPay_page import PerUnionPayPage
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_invoice_page import InvoicePage
from page.cert_seal_page import SealPage

class DxztbCase(Base):

    interfaceurl = Base.ip + "/testbpmsservice/org4SM2.jsp"
    url = Base.ip + "/dxztb2"
    if "59" in url:
        certbpms_value = [Base.ip+"/certbpms/RegisterCert.servlet","epoint","P003220170622001","T004001201904220001","1"]
    if "208" in url:
        certbpms_value = [Base.ip+"/certbpms/RegisterCert.servlet","pyptest","P000120180425001","T050101201904220001","1"]
    if "67" in url:
        certbpms_value = [Base.ip+"/certbpms/RegisterCert.servlet","epoint","P000320180517001","T000201201904220001","1"]

    def setUp(self):
        self.test = 0
        self.org4sm2page = Org4SM2Page(self.driver)
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.incompletepage = IncompletePage(self.driver)
        self.modifyInformationpage = ModifyInformationPage(self.driver)
        self.upfilepage = UpfilePage(self.driver)
        self.paypage = PayPage(self.driver)
        self.perunionpaypage = PerUnionPayPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)
        self.invoicepage = InvoicePage(self.driver)
        self.sealpage = SealPage(self.driver)

    def test_dxztb(self):
        business_number = self.interfaceOper()
        self.userOper(business_number)
        self.CertbpmsOper(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0:
            nowTime = self.now
            screenshot("电信招投标" + nowTime)  # 用例脚本运行报错立刻截图保存
        #self.driver.close()

    def interfaceOper(self):
        self.org4sm2page.open(self.interfaceurl)
        business_number = self.org4sm2page.applyCert(self.certbpms_value,self.data_org)
        #business_number = self.org4sm2page.postData(self.ip)
        return business_number

    def userOper(self, business_number):
        self.homepage.open(self.url)
        self.homepage.incomplete_button()
        self.userloginpage.loginUser(self.data_org)
        self.incompletepage.modifyInformation(business_number)
        #加载页面
        self.modifyInformationpage.reqid_text()
        self.modifyInformationpage.validmonth_select()
        self.modifyInformationpage.sealName_text("印章" + self.now)
        self.modifyInformationpage.submit_button()
        self.modifyInformationpage.alert()
        self.upfilepage.reqid_text()
        self.upfilepage.Upfile(closePDF=False)
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payOnDelivery_button()
        self.paypage.chooseElectronicInvoice(self.data_org)
        self.assertTrue(self.paypage.fee_text().startswith("40"))
        self.paypage.payCash()

    def CertbpmsOper(self, business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.checkpage.check_frame_in()
        self.checkpage.check_button()
        self.checkpage.searchBusiness(business_number)
        self.checkpage.detail_button()
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