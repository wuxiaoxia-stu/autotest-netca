
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage
from page.cert_seal_page import SealPage

'''
脚本信息：深圳政采业务用例
编写人：郭丹颖
编写时间：2020-4
'''
class BusinessCase(Base):
    
    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver) #初始化        
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)      
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)
        cls.SealPage = SealPage(cls.driver)

        cls.MenuPage.business_button()
        cls.BusinessPage.business_frame_in()
        cls.project = '深圳政采自动化测试项目'

    #用例：RSA证书申请
    def test_cert_business_01(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(self.project, '自动化测试-12RSA2048单位', '深圳政采RSA' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)    
        self.sleep(4)    
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例15-RSA证书申请完成')   
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()
    
    #用例：SM2证书和印章申请
    def test_cert_business_02(self):       
        self.BusinessPage.old_button()
        self.sleep()
        self.BusinessPage.selectUser_button()
        self.BusinessPage.submit_button()
        self.InfoPage.addInfo(self.project, '自动化测试-12SM2单位', '深圳政采SM2' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.CheckPage.exe('selectCert.exe')
        self.assertIn('成功', self.CheckResultPage.tipSeal_text())
        self.write_log('info', '用例15-SM2证书和印章申请完成')   

    @classmethod
    def tearDownClass(cls):
        cls.CheckResultPage.seal_button()
        cls.CheckResultPage.exe('selectCert.exe')
        cls.SealPage.delete_button()
        cls.SealPage.alert()    
        cls.SealPage.alert()     
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
    
     