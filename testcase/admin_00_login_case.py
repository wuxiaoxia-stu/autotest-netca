
from base import Base
from page.login_page import LoginPage

class AdminLoginCase(Base):

    #用例：登录综合管理系统
    def test_admin_login(self):
        page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            page.loginAdmin("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            page.loginAdmin(Base.ip, Base.n, Base.password)
        self.write_log('info', '用例0-登录综合管理系统完成')
 