
from base import Base
from page.admin_role_page import RolePage
from page.admin_menu_page import MenuPage


class RoleCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.roleName = '角色' + Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.role_button()
        cls.page = RolePage(cls.driver)
        cls.page.role_iframe_in()        

    #用例：添加角色
    def test_admin_role_01_add(self):
        self.page.addRole_button()
        self.page.parentBusinessCenterName_text('自动化测试业务中心')
        self.page.roleName_text(self.roleName)
        self.page.next_button()
        self.assertIn('成功', self.page.alert()) 
        self.write_log('info', '用例7-添加角色完成')
        self.sleep(1)  

    #用例：添加角色权限
    def test_admin_role_02_modify(self):
        self.page.busiOperation_button()
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例7-添加角色权限完成')
        self.sleep(1)


    '''
    #用例：查询角色
    def tst_admin_role_02_search(self):  
        self.page.roleName_text('自动化测试角色')
        self.page.search_button()
        

    #用例：修改角色
    def tst_admin_role_03_modify(self):  
        self.sleep() 
        self.page.detail_button()
        self.page.roleName_text('修改后')   
        self.page.submitM_button()   
        self.sleep(1)
        self.screenshot('修改角色')
        self.page.alert() 
    '''
    
    @classmethod
    def tearDownClass(cls):
        cls.page.role_iframe_out()
        cls.page.close_button()

        

