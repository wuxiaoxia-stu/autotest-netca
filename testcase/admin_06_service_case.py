
from base import Base
from page.admin_service_page import ServicePage
from page.admin_menu_page import MenuPage


class ServiceCase(Base):

    @classmethod
    def setUpClass(cls):        
        cls.projectName = '项目' + Base.now
        cls.serviceName = '用户服务' + Base.now   
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.service_button()
        cls.page = ServicePage(cls.driver)
        cls.page.service_iframe_in()          

    #用例：添加自助服务，依赖用例03‘添加项目’
    def test_admin_service_01_add(self):
        self.page.addService_button()
        self.page.serviceName_text(self.serviceName)
        self.page.projectName_text(self.projectName)
        self.sleep(1)
        self.page.templateName_text('管理系统自动化测试模板')
        self.page.reqType_button()
        self.page.feeMode_button()
        

        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例6-添加自助服务完成')
        self.sleep(1)

    #用例：查询自助服务
    def test_admin_service_02_search(self):
        self.page.serviceName_text(self.serviceName)
        self.page.search_button()
        self.page.detail_button()
        self.write_log('info', '用例6-查询自助服务完成')

    #用例：修改自助服务
    def test_admin_service_03_modify(self):
        self.page.serviceName_text('修改后')
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例6-修改自助服务完成')
        self.sleep(1)

    @classmethod
    def tearDownClass(cls):  
        cls.page.service_iframe_out()
        try:
            cls.page.dialog_close_button()
        except:
            pass
        cls.page.close_button()

        

