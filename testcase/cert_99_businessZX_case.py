
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_install_page import InstallPage
from page.cert_menu_page import MenuPage as CertMenuPage
from page.admin_user_page import UserPage
from page.admin_menu_page import MenuPage as AdminMenuPage
from page.login_page import LoginPage

#中信建投复审流程
class BusinessZXCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.reqID = ''

    #用例：初审
    def test_01_firstCheck(self):       
        self.page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            self.page.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            self.page.loginAdmin(Base.ip, Base.n, Base.password)
        self.page = AdminMenuPage(self.driver) #初始化
        self.page.user_button()
        self.page = UserPage(self.driver)
        self.page.user_iframe_in()     
        self.page.modifyUser(Base.operator, Base.parentBusinessCenterName, Base.firstBusinessCenterName)
        
        self.page = LoginPage(self.driver) #初始化
        self.page.loginCert(Base.ip, Base.firstBusinessCenterName, Base.n, Base.password)
        self.page = CertMenuPage(self.driver) #初始化
        self.page.business_button()
        self.page = BusinessPage(self.driver)
        self.page.business_frame_in()
        self.page.acceptBusiness('证书申请')
        self.page = InfoPage(self.driver)
        self.page.addInfo(Base.project_zx, Base.template_zx, '中信建投回归' + Base.now)
        self.page.submit_button()
               
        self.page = CheckPage(self.driver)
        BusinessZXCase.reqID = self.page.reqIDInfo_text()
        self.page.exportPDF(Base.win)
        self.page.checkBusiness(False)
        self.page.alert()
        self.write_log('info', '用例11-中信建投初审完成') 

    #用例：复审
    def test_02_cert_secondCheck(self):          
        self.page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            self.page.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            self.page.loginAdmin(Base.ip, Base.n, Base.password)
        self.page = AdminMenuPage(self.driver) #初始化
        self.page.user_button()
        self.page = UserPage(self.driver)
        self.page.user_iframe_in()     
        self.page.modifyUser(Base.operator, Base.firstBusinessCenterName, Base.secondBusinessCenterName)

        self.page = LoginPage(self.driver) #初始化
        self.page.loginCert(Base.ip, Base.secondBusinessCenterName, Base.n, Base.password)
        self.page = CertMenuPage(self.driver) #初始化
        self.page.business_button()
        self.page = CheckPage(self.driver)
        self.page.check_frame_in()
        self.page.check_button()
        self.page.searchBusiness(BusinessZXCase.reqID)
        self.page.detail_button()       
        self.page.checkBusiness(False)
        self.page = CheckResultPage(self.driver)
        self.assertIn('成功', self.page.tipCheck_text()) 
        self.write_log('info', '用例11-中信建投复审完成') 

    #用例：安装证书
    def test_03_cert_installCert(self):  
        self.page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            self.page.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            self.page.loginAdmin(Base.ip, Base.n, Base.password)
        self.page = AdminMenuPage(self.driver) #初始化
        self.page.user_button()
        self.page = UserPage(self.driver)
        self.page.user_iframe_in()     
        self.page.modifyUser(Base.operator, Base.secondBusinessCenterName, Base.firstBusinessCenterName)  

        self.page = LoginPage(self.driver) #初始化
        self.page.loginCert(Base.ip, Base.firstBusinessCenterName, Base.n, Base.password)
        self.page = CertMenuPage(self.driver) #初始化
        self.page.business_button()        
        self.page = InstallPage(self.driver)
        self.page.install_frame_in()
        self.page.install_button()
        self.page.installCert()
        self.page.install_frame_out()
        self.page.close_button()
        self.page = CertMenuPage(self.driver)        
        self.page.deleteCert()
        self.write_log('info', '用例11-中信建投安装证书完成') 
    
    @classmethod
    def tearDownClass(cls):        
        cls.page = LoginPage(cls.driver)
        if '192.168.0.67' in Base.ip:
            cls.page.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            cls.page.loginAdmin(Base.ip, Base.n, Base.password)
        cls.page = AdminMenuPage(cls.driver) #初始化
        cls.page.user_button()
        cls.page = UserPage(cls.driver)
        cls.page.user_iframe_in()     
        cls.page.modifyUser(Base.operator, Base.firstBusinessCenterName, Base.parentBusinessCenterName) 
        
