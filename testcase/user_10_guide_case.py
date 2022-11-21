from base import Base
from common.screenshot import screenshot
from page.user_home_page import HomePage
from page.user_guide_page import GuidePage
from page.user_login_page import UserLoginPage
from page.user_protocol_page import ProtocolPage
from page.user_incomplete_page import IncompletePage

#用例：检查自助服务证书使用指引
class GuideCase(Base):

    url = Base.ip + "/da"

    def setUp(self):
        self.test = 0
        self.homepage = HomePage(self.driver)
        self.guidepage = GuidePage(self.driver)
        self.userloginpage = UserLoginPage(self.driver)
        self.protocolpage = ProtocolPage(self.driver)
        self.incompletepage = IncompletePage(self.driver)

    def test_guide(self):
        self.userOper1()
        self.userOper2()
        self.test = 1

    def tearDown(self):
        if self.test == 0 :
            nowTime = self.now
            screenshot("指引"+nowTime)#用例脚本运行报错立刻截图保存
        #self.driver.close()

    def userOper1(self):
        self.homepage.open(self.url)
        self.homepage.guide_button()
        self.guidepage.firstGuide_button()
        self.assertTrue(self.guidepage.guideTitle_text().startswith("这是一条指引"))
        self.assertTrue(self.guidepage.guideContent_text().startswith("这是一条指引"))

    #未完成业务提醒
    def userOper2(self):
        self.homepage.open(self.url)
        self.homepage.apply_button()
        self.userloginpage.loginUser(self.data_org)
        self.assertTrue(self.protocolpage.title_text().startswith("网证通电子认证服务协议"))
        self.protocolpage.quit_button()
        self.homepage.apply_button()
        self.userloginpage.loginUser(self.data_org,apply=False)
        self.userloginpage.goFinish_button()
        self.assertTrue(self.incompletepage.title_text().startswith("业务状态查询结果"))
