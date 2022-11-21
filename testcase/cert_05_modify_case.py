
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_modify_page import ModifyPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage

'''
脚本信息：业务修改用例
编写人：郭丹颖
编写时间：2018-5
'''
class ModifyCase(Base):
 
    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver) #初始化
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)
        cls.CheckPage = CheckPage(cls.driver)
        cls.ModifyPage = ModifyPage(cls.driver)
        cls.MenuPage.business_button()
        cls.BusinessPage.business_frame_in()

    #用例：业务修改
    def test_cert_modify(self):  
        self.page = BusinessPage(self.driver) 
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '业务修改' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.modify_button() #点击修改
        self.ModifyPage.userName_text('修改后用户名称'+ Base.now)
        self.ModifyPage.isNeedSeal_button()
        self.ModifyPage.submitModify_button() #提交
        self.assertIn('成功', self.ModifyPage.tipModify_text())
        self.write_log('info', '用例4-业务修改完成') 
        self.ModifyPage.check_button() #点击审核
        self.CheckPage.checkBusiness(False)      

    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()
