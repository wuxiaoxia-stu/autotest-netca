
import random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

#测试项目需要配置：RSA+SM2
'''
脚本信息：同时申请RSA+SM2用例
编写人：郭丹颖
编写时间：2018-5
'''
class RSASM2Case(Base):

    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver)
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)
        cls.MenuPage.business_button()   
        cls.template = '自动化测试-12RSA2048个人'

    #用例：同时申请RSA和SM2证书
    def test_cert_01_SM2business(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '用户名' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.sleep(2)
        self.CheckResultPage.registerSM2()
        self.assertIn('成功', self.CheckResultPage.tipSM2_text())
        self.write_log('info', '用例9-申请RSA和SM2证书完成') 
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
