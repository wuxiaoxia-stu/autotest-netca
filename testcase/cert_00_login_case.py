
from base import Base
from page.login_page import LoginPage
from page.cert_bottom_page import BottomPage
import re

class CertLoginCase(Base):

    #用例：登录证书业务系统
    def test_cert_login(self):
        page = LoginPage(self.driver) #初始化
        page.loginCert(Base.ip, Base.parentBusinessCenterName, Base.n, Base.password)

        page = BottomPage(self.driver)
        page.bottom_iframe_in()
        Base.operator = page.bottom_text().split()[1]
        page.bottom_iframe_out()
        self.write_log('info', '用例0-登录证书业务系统完成')

