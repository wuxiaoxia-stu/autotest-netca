
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_infoAppl_page import InfoApplPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

'''
脚本信息：应用业务用例
编写人：郭丹颖
编写时间：2018-5
'''
class ApplicationCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver) #初始化
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)
        cls.InfoApplPage = InfoApplPage(cls.driver)
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)
        cls.MenuPage.business_button()
        cls.BusinessPage.business_frame_in()
        cls.BusinessPage.acceptBusiness('证书申请')
        cls.InfoPage.addInfo(Base.project, Base.template, '应用回归' + Base.now)
        cls.InfoPage.submit_button()
        cls.CheckPage.checkBusiness(False)        
        cls.CheckResultPage.continue_button()
        cls.CheckPage.back_button()

    #用例：应用开通
    def test_cert_application_01(self):   
        self.BusinessPage.acceptBusiness('应用开通', 1)
        self.InfoApplPage.appl_button()
        self.InfoApplPage.endtime_button()
        self.InfoApplPage.endtime_frame_in()
        self.InfoApplPage.endtimeHour_text(23)
        self.InfoApplPage.endtimeSubmit_button()
        self.InfoApplPage.endtime_frame_out()
        self.InfoApplPage.month_text(0)
        self.InfoApplPage.getInfo(Base.template)
        self.InfoApplPage.submit_button()
        self.CheckPage.submit_button()
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例5-应用开通完成') 
        self.CheckResultPage.continue_button()

    #用例：缩短应用有效期
    def test_cert_application_02(self):   
        self.BusinessPage.acceptBusiness('缩短应用有效期', 1)
        self.InfoApplPage.appl_button()
        self.InfoApplPage.endtime_button()
        self.InfoApplPage.endtime_frame_in()
        self.InfoApplPage.endtimeSubmit_button()
        self.InfoApplPage.endtime_frame_out()
        self.InfoApplPage.getInfo(Base.template)
        self.InfoApplPage.submit_button()
        self.CheckPage.submit_button()
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例5-缩短应用有效期完成') 
        self.CheckResultPage.continue_button()

    #用例：延长应用有效期
    def test_cert_application_03(self):   
        self.BusinessPage.acceptBusiness('延长应用有效期', 1)
        self.InfoApplPage.appl_button()
        self.InfoApplPage.endtime_button()
        self.InfoApplPage.endtime_frame_in()
        self.InfoApplPage.endtimeHour_text(23)
        self.InfoApplPage.endtimeSubmit_button()
        self.InfoApplPage.endtime_frame_out()
        self.InfoApplPage.month_text(0)
        self.InfoApplPage.getInfo(Base.template)
        self.InfoApplPage.submit_button()
        self.CheckPage.submit_button()
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例5-延长应用有效期完成') 
        self.CheckResultPage.continue_button()

    #用例：取消应用
    def test_cert_application_04(self):   
        self.BusinessPage.acceptBusiness('应用取消', 1)
        self.InfoApplPage.appl_button()
        self.InfoApplPage.getInfo(Base.template)
        self.InfoApplPage.submit_button()
        self.CheckPage.submit_button()
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例5-取消应用完成') 

    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()