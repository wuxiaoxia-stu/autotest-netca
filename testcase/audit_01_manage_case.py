
from base import Base
from page.audit_manage_page import ManagePage
from page.audit_menu_page import MenuPage
import unittest


class Manage(Base):

    @classmethod
    def setUpClass(cls): 
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.manage_button()
        cls.page = ManagePage(cls.driver)
        cls.page.manage_iframe_in()        

    #用例：查询审计管理
    def test_audit_manage(self):
        self.page.search_button()
        self.screenshot('审计查询')

    @classmethod
    def tearDownClass(cls):
        cls.page.manage_iframe_out()
        cls.page.close_button()

        

