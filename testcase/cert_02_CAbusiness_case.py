
import random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

#测试项目需要配置：换CA
#需要安装较新版本客户端（能自动删除旧证书）
'''
脚本信息：换CA用例
编写人：郭丹颖
编写时间：2018-5
'''
class CABusinessCase(Base):

    template = '自动化测试-06RSA1024员工'
    identityType = Base.data_cert[2]
    identity = Base.data_cert[3]
    userName = '换CA回归' + Base.now
    countryName = Base.data_cert[5]
    province = Base.data_cert[6]
    city = Base.data_cert[7]
    phone = Base.data_cert[8]
    email = Base.data_cert[9]
    department = Base.data_cert[10]
    residence = Base.data_cert[11]
    mytype = Base.data_cert[12]
    
    oIdentityType = Base.data_cert[13]
    oIdentity = Base.data_cert[14]
    oUserName = Base.data_cert[15]
    oCountryName = Base.data_cert[16]
    oProvince = Base.data_cert[17]
    oPhone = Base.data_cert[18]
    oResidence = Base.data_cert[19]
    oType = Base.data_cert[20]

    lIdentityType = Base.data_cert[21]
    lIdentity = Base.data_cert[22]
    lName = Base.data_cert[23]
    lPhone = Base.data_cert[24]
    lEmail = Base.data_cert[25]


    def setUp(self):
        self.MenuPage = MenuPage(self.driver)
        self.BusinessPage = BusinessPage(self.driver)
        self.MenuPage.business_button()  
        self.InfoPage = InfoPage(self.driver)
        self.CheckPage = CheckPage(self.driver)
        self.CheckResultPage = CheckResultPage(self.driver)


    #用例：换CA续期选回普通续期
    def test_cert_CAbusiness_01(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')       
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button() 
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书续期', 1)
        self.InfoPage.changeCA_button()
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.assertIn('成功', self.CheckResultPage.tip_text())    
        self.write_log('info', '用例2-换CA续期选回普通续期完成')    

    #用例：换CA续期
    def test_cert_CAbusiness_02(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书续期', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例2-换CA续期完成')


    #用例：换CA更新    
    def test_cert_CAbusiness_03(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书密钥更新', 1)
        self.assertFalse(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例2-换CA更新完成')  

    #用例：换CA变更
    def test_cert_CAbusiness_04(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书变更', 1)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例2-换CA变更完成')  

    #用例：换CA补办
    def test_cert_CAbusiness_05(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('证书补办', 1)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例2-换CA补办完成')  

    #用例：换CA密匙更换
    def test_cert_CAbusiness_06(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('电子密匙更换', 1)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例2-换CA补办完成')  

    #用例：换CA重新制证
    def test_cert_CAbusiness_07(self):           
        self.BusinessPage.business_frame_in()
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.CAproject, self.template, '换CA回归' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False)        
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

        self.BusinessPage.acceptBusiness('重新制证', 1)
        self.assertTrue(self.InfoPage.getSealAttribute())
        self.InfoPage.getInfo(self.template)
        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)        
        self.assertIn('成功', self.CheckResultPage.tip_text()) 
        self.write_log('info', '用例2-换CA重新制证完成')  

    def tearDown(self):
        self.CheckPage.sleep(3)  # 添加延迟，不然审核页面自动删除旧证书会弹窗报错：无效的调用过程或参数
        self.BusinessPage.business_frame_out()
        self.BusinessPage.close_button()
        self.MenuPage.deleteCert()
