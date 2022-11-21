import platform
from base import Base
from page.cert_pin_page import PinPage
from page.cert_menu_page import MenuPage


class PinCase(Base):

     
    @classmethod
    def setUpClass(cls):
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.pin_button()
        cls.page = PinPage(cls.driver)
        cls.page.pin_iframe_in()

    #用例：重置管理员密码
    def test_cert_pin_01_resetAdminpin(self):              
        self.page.adminPin_button()
        self.sleep(1)
        self.page.getAdminPin_button()
        self.sleep(1)
        self.page.generate_button()
        self.sleep(1)
        self.page.set_button()
        self.page.alert() 
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例1-重置管理员密码完成')
        self.sleep(1)
          
    #用例：重置用户密码
    def test_cert_pin_02_resetPin(self): 
        if Base.win == '10':
            self.page.print_button()
        self.page.pinNum_text('12345678')
        self.page.set_button()
        self.page.alert() 
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例1-重置用户密码完成')
        if Base.win == '7':
            self.page.exe('print.exe ' + Base.win + ' 密码信封')

    @classmethod
    def tearDownClass(cls):
        cls.page.pin_iframe_out()
        cls.page.close_button()
       

