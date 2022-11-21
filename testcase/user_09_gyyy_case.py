from base import Base
from common.screenshot import screenshot
from common import TraverseDevice
from common import KeyRegedit
from page.login_page import LoginPage
from page.cert_menu_page import MenuPage
from page.cert_batch_page import BatchPage
from page.user_home_page import HomePage
from page.user_login_page import UserLoginPage
from page.user_incomplete_page import IncompletePage
from page.user_modifyInformation_page import ModifyInformationPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage

class GyyyCase(Base):

    url = Base.ip + "/autogyyy"
    project = ["自动化测试项目（叶）","自动化广医一院员工"]
    keynum = TraverseDevice.GetDeviceNum()

    def setUp(self):
        self.test = 0
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.batchpage = BatchPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.incompletepage = IncompletePage(self.driver)
        self.modifyInformationpage = ModifyInformationPage(self.driver)
        self.checkpage = CheckPage(self.driver)
        self.checkresultpage = CheckResultPage(self.driver)

    def test_gyyy(self):
        business_number = self.CertbpmsOper1()
        self.userOper1(business_number)
        self.CertbpmsOper2(business_number)
        self.userOper2(business_number)
        self.CertbpmsOper3()
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("广医一院"+nowTime)#用例脚本运行报错立刻截图保存
        KeyRegedit.ChangeRegedit(self.keynum, "put")
        #self.driver.close()

    #证书业务系统，批量处理，上传附件
    def CertbpmsOper1(self):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName,Base.n,Base.password)
        self.menupage.business_button()
        self.batchpage.batch_frame_in()
        self.batchpage.batch_button()
        self.batchpage.project_text(self.project[0])
        self.batchpage.template_text(self.project[1])
        self.batchpage.need_radio()
        self.batchpage.upload_button()
        self.sleep(1)
        self.batchpage.exe('upload_type1.exe gyyy.xls')
        self.sleep(1)
        self.batchpage.summit_button()
        self.batchpage.goCheck_button()
        business_number = self.batchpage.businessNum_text()
        return business_number

    #自助服务系统，修改资料，上传证书请求
    def userOper1(self,business_number):
        KeyRegedit.ChangeRegedit(self.keynum,"pull")
        self.homepage.open(self.url)
        self.homepage.incomplete_button()
        self.userloginpage.loginUser(self.data_org)
        self.incompletepage.modifyInformation(business_number)
        self.modifyInformationpage.mendifyInformation(self.data_staff)
        KeyRegedit.ChangeRegedit(self.keynum, "put")

    def CertbpmsOper2(self,business_number):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.menupage.business_button()
        self.checkpage.check_frame_in()
        self.checkpage.check_button()
        self.checkpage.searchBusiness(business_number)
        self.checkpage.detail_button()
        self.checkpage.submit_button()
        self.checkresultpage.continue_button()

    def userOper2(self,business_number):
        self.homepage.open(self.url)
        self.homepage.incomplete_button()
        self.incompletepage.installCert(business_number)

    def CertbpmsOper3(self):
        self.loginpage.loginCert(Base.ip, Base.parentBusinessCenterName, str(int(Base.n)+1), Base.password)
        self.menupage.deleteCert()