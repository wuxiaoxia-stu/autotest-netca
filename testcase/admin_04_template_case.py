
from base import Base
from page.admin_template_page import TemplatePage
from page.admin_menu_page import MenuPage


class TemplateCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.templateName = '模板' + Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.template_button()
        cls.page = TemplatePage(cls.driver)
        cls.page.template_iframe_in()        

    #用例：添加证书模板
    def test_admin_template_01_add(self):
        self.page.addTemplate_button()
        self.page.templateName_text(self.templateName)
        self.page.parentBusinessCenterName_text(Base.parentBusinessCenterName)
        self.page.CAtemplateName_text('自动化测试CA模板')
        self.sleep()
        self.page.addCATemplate_button()
        self.page.addCATemplate_button()
        self.sleep()
        self.page.addSubject_button()
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例4-添加证书模板完成')
        self.sleep(1)

    #用例：查询证书模板
    def test_admin_template_02_search(self):
        self.page.templateName_text(self.templateName)
        self.page.search_button()
        self.write_log('info', '用例4-查询证书模板完成')

    #用例：修改证书模板
    def test_admin_template_03_modify(self):
        self.page.detail_button()
        self.page.templateName_text('修改后')
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例4-修改证书模板完成')
        self.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.page.template_iframe_out()
        try:
            cls.page.dialog_close_button()
        except:
            pass
        cls.page.close_button()

        

