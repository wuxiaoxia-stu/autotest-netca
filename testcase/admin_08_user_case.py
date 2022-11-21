
from base import Base
from page.admin_user_page import UserPage
from page.admin_menu_page import MenuPage


class UserCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.userName = '用户' + Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.user_button()
        cls.page = UserPage(cls.driver)
        cls.page.user_iframe_in()

    #用例：添加用户
    def test_admin_user_01_add(self):
        self.page.addUser_button()
        self.page.userName_text(self.userName)
        self.page.parentBusinessCenterName_select1('自动化测试业务中心')
        self.page.moveRight_button()
        self.page.identityType_select('工作证')
        self.page.identity_text('0409')       
        self.page.uploadCert('修改后用户名称-签名证书.cer')       
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())  
        self.write_log('info', '用例8-添加用户完成')  
        self.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.page.user_iframe_out()
        cls.page.close_button()

        

