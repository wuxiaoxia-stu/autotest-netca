
from base import Base
from page.audit_log_page import LogPage
from page.audit_menu_page import MenuPage
import unittest


class Log(Base):

    @classmethod
    def setUpClass(cls): 
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.log_button()
        cls.page = LogPage(cls.driver)
        cls.page.log_iframe_in()        

    #用例：查询审计管理
    def test_audit_01_log(self):
        self.page.fileName_text('catalina.out')
        self.page.queryType_select('从尾向前查询')
        self.page.search_button()
        self.screenshot('日志查询')

    #用例：下载日志
    '''
    def test_audit_02_download(self):
        self.page.download_button()
        print('1111111111')
        #self.page.exe('download.exe ' + Base.win + ' 电子发票')  
'''
    @classmethod
    def tearDownClass(cls):
        cls.page.log_iframe_out()
        cls.page.close_button()
