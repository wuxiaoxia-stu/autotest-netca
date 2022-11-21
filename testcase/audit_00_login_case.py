
from base import Base
from page.login_page import LoginPage

class AuditLoginCase(Base):

    #用例：登录审计系统
    def test_audit_login(self):
        page = LoginPage(self.driver)
        if '192.168.0.67' in Base.ip:
            page.loginAudit("http://192.168.0.50:8080", Base.n, Base.password)
        else:
            page.loginAudit(Base.ip, Base.n, Base.password)
        self.write_log('info', '用例0-登录审计系统完成')
