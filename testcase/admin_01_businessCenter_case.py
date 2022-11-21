
from base import Base
from page.admin_businessCenter_page import BusinessCenterPage
from page.admin_menu_page import MenuPage
import unittest

'''
脚本信息：业务中心用例
编写人：郭丹颖
编写时间：2018-5
'''
class BusinessCenterCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.businessCenterName = '业务中心' + Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.businessCenter_button()
        cls.page = BusinessCenterPage(cls.driver)
        cls.page.businessCenter_iframe_in()        

    #用例：添加业务中心
    def test_admin_businessCenter_01_add(self):
        self.page.addBusinessCenter_button()
        self.page.parentBusinessCenterName_text(Base.parentBusinessCenterName)
        self.page.businessCenterName_button()
        self.page.businessCenterName_text(self.businessCenterName)        
        self.page.organization_text('服务单位')
        self.sleep()
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例1-添加业务中心完成')
        self.sleep(1)
                  
    #用例：查询业务中心
    def test_admin_businessCenter_02_search(self):
        self.page.businessCenterName_text(self.businessCenterName) 
        self.page.search_button()
        self.write_log('info', '用例1-查询业务中心完成')

    #用例：修改业务中心
    def test_admin_businessCenter_03_modify(self):
        self.page.detail_button()
        self.page.organization_text('修改后') 
        self.page.submitModify_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例1-修改业务中心完成')
        self.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.page.businessCenter_iframe_out()
        cls.page.close_button()

