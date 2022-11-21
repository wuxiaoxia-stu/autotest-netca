import random
from base import Base
from common.screenshot import screenshot
from page.user_nanwang_page import NanwangPage
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

#用例：南网项目用户自助（如59，https://192.168.0.59/usercertservice/nfqytydljyptindex.jsp）
#业务信息：南网页面选择证书套餐，定制费用。
class NanwangCase(Base):

    url = Base.ip + "/usercertservice/nfqytydljyptindex.jsp"
    orgBaseFee = ['140','350','580']
    orgComposeFee = ['240','600','1000']
    staffBaseFee = ['120','300','500']
    staffComposeFee = ['200','500','800']
    allFee = {"orgBase":orgBaseFee,"orgCompose":orgComposeFee,"staffBase":staffBaseFee,"staffCompose":staffComposeFee}

    def setUp(self):
        self.test = 0
        self.nanwangpage = NanwangPage(self.driver)
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

    def test_nanwang(self):
        self.userOper1()
        business_number = self.userOper2()
        self.CertbpmsOper1(business_number)
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("南网"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        # 机构基础
        self.nanwangpage.open(self.url)
        self.nanwangpage.orgBase_button()
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        fees = self.serviceinformationPage.returnFee()
        self.checkFee(fees,"orgBase")
        # 机构组合
        self.nanwangpage.open(self.url)
        self.nanwangpage.orgCompose_button()
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        fees = self.serviceinformationPage.returnFee()
        self.checkFee(fees,"orgCompose")
        # 员工基础
        self.nanwangpage.open(self.url)
        self.nanwangpage.staffBase_button()
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        fees = self.serviceinformationPage.returnFee()
        self.checkFee(fees,"staffBase")
        # 员工组合
        self.nanwangpage.open(self.url)
        self.nanwangpage.staffCompose_button()
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        fees = self.serviceinformationPage.returnFee()
        self.checkFee(fees,"staffCompose")


    def userOper2(self):
        self.nanwangpage.open(self.url)
        self.nanwangpage.orgBase_button()
        self.homepage.apply_button()
        self.protocolpage.agree_button()
        self.serviceinformationPage.agree_button()
        self.userinfopage.writeOrgInfo(self.now,self.data_org)
        self.userinfopage.validity_select("12")
        self.userinfopage.sealName_text("印章" + self.now)
        self.userinfopage.submit()
        self.userinfopage.alert()
        self.userinfopage.alert()
        business_number = self.upfilepage.Upfile()
        self.upfilepage.submit_button()
        self.upfilepage.nextStep_button()
        self.paypage.payByBusiness_Button()
        self.paypage.chooseVatInvoice()
        self.paypage.chooseBankTransfer()
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
        self.invoicepage.newZhuanpiao(random.randint(10000000, 99999999), '012345678000', 20)
        self.checkresultpage.continue_button()
        self.sealpage.seal_button()
        self.sealpage.deleteSeal()
        self.sealpage.iframe_out()
        self.menupage.deleteCert()

    def checkFee(self,Fees,choose):
        targetFee = self.allFee[choose]
        self.assertIn('1',Fees[0][0])
        self.assertIn(targetFee[0],Fees[0][1])
        self.assertIn('3', Fees[1][0])
        self.assertIn(targetFee[1], Fees[1][1])
        self.assertIn('5', Fees[2][0])
        self.assertIn(targetFee[2], Fees[2][1])




