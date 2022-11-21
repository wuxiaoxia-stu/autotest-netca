
import platform
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage as CertMenuPage
from page.admin_user_page import UserPage
from page.admin_menu_page import MenuPage as AdminMenuPage
from page.login_page import LoginPage

'''
脚本信息：深圳质监复审用例
编写人：郭丹颖
编写时间：2018-5
'''
class BusinessSZCase(Base):

     
    @classmethod
    def setUpClass(cls):
        cls.reqID = ''
        cls.LoginPage = LoginPage(cls.driver)
        cls.AdminMenuPage = AdminMenuPage(cls.driver) #初始化
        cls.UserPage = UserPage(cls.driver)
        cls.page = LoginPage(cls.driver) #初始化
        cls.CertMenuPage = CertMenuPage(cls.driver) #初始化
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)

    #用例：初审
    def test_01_firstCheck(self):              
        if '192.168.0.67' in Base.ip:
            self.LoginPage.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            self.LoginPage.loginAdmin(Base.ip, Base.n, Base.password)
        self.AdminMenuPage.user_button()
        self.UserPage.user_iframe_in()     
        self.UserPage.modifyUser(Base.operator, Base.parentBusinessCenterName, Base.BusinessCenterName_sz)
        
        self.sleep()
        self.LoginPage.loginCert(Base.ip, Base.BusinessCenterName_sz, Base.n, Base.password)
        self.CertMenuPage.business_button()
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project_sz, Base.template_sz, '深圳质监回归' + Base.now)
        self.InfoPage.submit_button()               
        BusinessSZCase.reqID = self.CheckPage.reqIDInfo_text()
        self.CheckPage.checkBusiness(False)
        self.write_log('info', '用例8-深圳质监初审完成') 

    #用例：复审
    def test_02_cert_secondCheck(self):          
        self.page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            self.LoginPage.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            self.LoginPage.loginAdmin(Base.ip, Base.n, Base.password)
        self.AdminMenuPage.user_button()
        self.UserPage.user_iframe_in()     
        self.UserPage.modifyUser(Base.operator, Base.BusinessCenterName_sz, Base.parentBusinessCenterName)

        self.sleep()
        self.LoginPage.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)
        self.CertMenuPage.business_button()
        self.CheckPage.check_frame_in()
        self.CheckPage.check_button()
        self.CheckPage.searchBusiness(BusinessSZCase.reqID)
        self.CheckPage.detail_button()       
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例8-深圳质监复审完成') 

     
    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.CertMenuPage.deleteCert()
