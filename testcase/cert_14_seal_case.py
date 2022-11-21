
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_seal_page import SealPage
from page.cert_menu_page import MenuPage

'''
脚本信息：国密印章用例
编写人：郭丹颖
编写时间：2019-12
'''
class SealCase(Base):
    
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
    
    #用例：写入印章
    def test_cert_seal_01(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '国密印章回归' + Base.now)
        sealName = '国密印章名称' + Base.now
        self.InfoPage.sealName_text(sealName)
        self.InfoPage.submit_button()
        self.assertEqual(sealName, self.CheckPage.getSealName())
        self.CheckPage.checkBusiness(True, True)
        self.sleep(4)  
        self.CheckResultPage.seal_button()
        self.SealPage.uploadFile(Base.win, 'seal.jpg') 
        self.SealPage.writeSeal_button()
        self.sleep(2)
        self.assertIn('成功', self.SealPage.alert())

    #用例：删除印章
    def test_cert_seal_02(self):
        self.SealPage.delete_button()
        self.SealPage.alert()
        self.assertIn('成功', self.SealPage.alert())
	
    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
    
