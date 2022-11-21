
from base import Base
from page.admin_project_page import ProjectPage
from page.admin_menu_page import MenuPage


class ProjectCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.projectName = '项目' + Base.now

    #用例：添加项目
    def test_admin_project_add(self):
        self.page = MenuPage(self.driver) #初始化
        self.page.project_button()
        self.page = ProjectPage(self.driver)
        self.page.project_iframe_in()
        self.page.addProject_button()
        self.page.projectName_text(self.projectName)
        self.page.projectNo_text('201901090109')
        self.page.parentBusinseeCenterName_select(Base.parentBusinessCenterName)
        self.page.move_button()
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例3-添加项目完成')
        self.sleep(1)

    def tearDown(self):
        self.page.project_iframe_out()
        self.page.close_button()
       

