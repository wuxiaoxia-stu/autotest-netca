
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

'''
脚本信息：证书业务用例
编写人：郭丹颖
编写时间：2018-5
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

        cls.identityType = Base.data_cert[2]
        cls.identity = Base.data_cert[3]
        cls.userName = '用户名' + Base.now
        cls.countryName = Base.data_cert[5]
        cls.province = Base.data_cert[6]
        cls.city = Base.data_cert[7]
        cls.phone = Base.data_cert[8]
        cls.email = Base.data_cert[9]
        cls.department = Base.data_cert[10]
        cls.residence = Base.data_cert[11]
        cls.type = Base.data_cert[12]
        
        cls.oIdentityType = Base.data_cert[13]
        cls.oIdentity = Base.data_cert[14]
        cls.oUserName = Base.data_cert[15]
        cls.oCountryName = Base.data_cert[16]
        cls.oProvince = Base.data_cert[17]
        cls.oPhone = Base.data_cert[18]
        cls.oResidence = Base.data_cert[19]
        cls.oType = Base.data_cert[20]

        cls.lIdentityType = Base.data_cert[21]
        cls.lIdentity = Base.data_cert[22]
        cls.lName = Base.data_cert[23]
        cls.lPhone = Base.data_cert[24]
        cls.lEmail = Base.data_cert[25]


    #用例：证书申请
    def test_cert_business_01(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.addInfo(Base.project, Base.template, '业务回归' + Base.now)
        self.InfoPage.uploadFile(Base.win, 'untitled.png')
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)  
        self.sleep(2)      
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-证书申请完成')   
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()


    #用例：证书续期
    def test_cert_business_02(self):           
        self.BusinessPage.acceptBusiness('证书续期', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-证书续期完成')   
        self.CheckResultPage.continue_button()


    #用例：证书密钥更新
    def test_cert_business_03(self):           
        self.BusinessPage.acceptBusiness('证书密钥更新', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-证书密钥更新完成')   
        self.CheckResultPage.continue_button()

    #用例：证书变更
    def test_cert_business_04(self):           
        self.BusinessPage.acceptBusiness('证书变更', 1)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-证书变更完成')   
        self.CheckResultPage.continue_button()

    #用例：证书挂失
    def test_cert_business_05(self):           
        self.BusinessPage.acceptBusiness('证书挂失', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例3-证书挂失完成')   
        self.CheckResultPage.continue_button()

    #用例：证书解挂
    def test_cert_business_06(self):           
        self.BusinessPage.acceptBusiness('证书解挂', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例3-证书解挂完成')   
        self.CheckResultPage.continue_button()

    #用例：证书注销
    def test_cert_business_07(self):           
        self.BusinessPage.acceptBusiness('证书注销', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例3-注销完成')   
        self.CheckResultPage.continue_button()

    #用例：证书申请+补办
    def test_cert_business_08(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '业务回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书补办', 2)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-补办完成')   
        self.CheckResultPage.continue_button()       
    
    #用例：电子密匙更换
    def test_cert_business_09(self):           
        self.BusinessPage.acceptBusiness('电子密匙更换', 3)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.nokey_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-电子密匙更换完成')   
        self.CheckResultPage.continue_button()

    #用例：用户退订
    def test_cert_business_10(self):           
        self.BusinessPage.acceptBusiness('用户退订', 4)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)
        self.assertIn('成功', self.CheckResultPage.tipCheck_text())
        self.write_log('info', '用例3-用户退订完成')   
        self.CheckResultPage.continue_button()       

    #用例：证书申请+重新制证
    def test_cert_business_11(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '业务回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('重新制证', 5)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-重新制证完成')   
        self.CheckResultPage.continue_button()

    # 用例：密钥恢复
    def test_cert_business_12(self):
        self.BusinessPage.acceptBusiness('密钥恢复', 5)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(Base.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('1张证书已经安装成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例3-密钥恢复完成')
        self.CheckResultPage.continue_button()


    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
    
     