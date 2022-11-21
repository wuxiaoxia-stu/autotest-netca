
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

'''
脚本信息：机构信息查询用例
编写人：郭丹颖
编写时间：2019-8
'''
class BusinessCase(Base):
    
    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver) #初始化        
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)      
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)

        cls.MenuPage.business_button()
        cls.BusinessPage.business_frame_in()
    
    #用例1：机构证书机构信息查询
    def test_cert_business_01(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.project_text(Base.project)
        self.InfoPage.template_text('自动化测试-12SM2单位')
        self.InfoPage.orgIdentity_text('广东省电子商务认证有限公司')
        self.InfoPage.orgSearch_button()
        self.InfoPage.sleep(6)
        self.assertIn('广东省电子商务认证有限公司', self.InfoPage.getUserName_text())
        self.InfoPage.lIdentityType_select('1')
        self.InfoPage.lIdentity_text('236504195106192666')
        self.InfoPage.lName_text('经办人')
        self.InfoPage.lPhone_text('15626480142')
        self.InfoPage.lEmail_text('zs@cnca.net')
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)              
        self.write_log('info', '用例1-机构信息查询完成')
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

    #用例2：员工证书机构信息查询
    def test_cert_business_02(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.project_text(Base.project)
        self.InfoPage.template_text('自动化测试-12SM2员工')
        self.InfoPage.orgIdentity_text('广东省电子商务认证有限公司')
        self.InfoPage.orgSearch_button()
        self.InfoPage.sleep(4)
        self.assertIn('广东省电子商务认证有限公司', self.InfoPage.getOUserName_text())
        self.InfoPage.identityType_select('1')
        self.InfoPage.identity_text('236504195106192666')
        self.InfoPage.userName_text('测试'+Base.now)
        self.InfoPage.countryName_select('中国')
        self.InfoPage.province_select('广东')
        self.InfoPage.department_text('测试部门')
        self.InfoPage.residence_text('测试地址')
        self.InfoPage.type_select('1')
        self.InfoPage.lIdentityType_select('1')
        self.InfoPage.lIdentity_text('236504195106192666')
        self.InfoPage.lName_text('经办人')
        self.InfoPage.lPhone_text('15626480142')
        self.InfoPage.lEmail_text('zs@cnca.net')
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)              
        self.write_log('info', '用例1-机构信息查询完成') 

    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
    
     