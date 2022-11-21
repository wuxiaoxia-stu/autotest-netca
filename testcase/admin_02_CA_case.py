

from base import Base
from page.admin_CA_page import CAPage
from page.admin_menu_page import MenuPage


class CACase(Base):

    @classmethod
    def setUpClass(cls):
        cls.CATemplateNmae = 'CA模板' + Base.now
        cls.CATemplateId = Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.CA_button()
        cls.page = CAPage(cls.driver)
        cls.page.CA_iframe_in()   
        cls.page.CATemplate_button()            

    #用例：添加CA模板
    def test_admin_CA_01_add(self):
        self.page.addCATemplate_button()
        self.page.CATemplateName_text(self.CATemplateNmae)
        self.page.CATemplateId_text(self.CATemplateId)
        self.page.submit_button()
        self.assertIn('成功', self.page.alert()) 
        self.write_log('info', '用例2-添加CA模板完成')
        self.sleep(1)

    #用例：查询CA模板
    def test_admin_CA_02_search(self):
        self.page.CATemplateNameS_text(self.CATemplateNmae)
        self.page.search_button()
        self.write_log('info', '用例2-查询CA模板完成')

    #用例：修改CA模板
    def test_admin_CA_03_modify(self):
        self.page.detail_button()
        self.page.CATemplateNameM_text('修改后')
        self.page.submitM_button()
        self.assertIn('成功', self.page.alert()) 
        self.write_log('info', '用例2-修改CA模板完成')
        self.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.page.CA_iframe_out()
        cls.page.close_button()
       

