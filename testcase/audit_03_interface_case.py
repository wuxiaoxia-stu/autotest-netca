
from base import Base
from page.audit_interface_page import InterfacePage
from page.audit_menu_page import MenuPage
import unittest


class Interface(Base):

    @classmethod
    def setUpClass(cls): 
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.interface_button()
        cls.page = InterfacePage(cls.driver)    
        cls.page.interface_frame_in() 

    #用例：查询第三方接口通信日志
    def test_audit_interface_01(self):
        self.screenshot('第三方接口通信日志查询')

    
    #用例：第三方接口通信日志详情
    def test_audit_interface_02(self):
        self.page.more_button()
        self.screenshot('第三方接口通信日志详情')
        self.page.return_button()

    #用例：第三方接口通信日志审计
    def test_audit_interface_03(self):
        self.page.selectAll_button()
        self.page.batchAudit_button()
        self.page.alert()
        self.assertIn('成功', self.page.alert())


    @classmethod
    def tearDownClass(cls):
        cls.page.interface_frame_out() 
        cls.page.close_button()

        

