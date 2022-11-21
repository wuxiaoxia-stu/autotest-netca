import unittest
from base import Base
from page.admin_projectSearch_page import ProjectSearchPage
from page.admin_projectIndi_page import ProjectIndiPage
from page.admin_menu_page import MenuPage
from page.admin_projectSetLinkman_page import ProjectSetLinkmanPage
from page.admin_projectSetSubBC_page import ProjectSetSubBCPage
from page.admin_projectSetPush_page import ProjectSetPushPage
from page.admin_projectSetTemplate_page import ProjectSetTemplatePage
from page.admin_projectSetApplicat_page import ProjectSetApplicatPage
from page.admin_projectSetCost_page import ProjectSetCostPage
from page.admin_projectSetExpress_page import ProjectSetExpressPage
from page.admin_projectSetData_page import ProjectSetDataPage
from page.admin_projectSetFile_page import ProjectSetFilePage

'''
脚本信息：业务中心用例
编写人：郭丹颖
编写时间：2018-5
'''
class ProjectIndiCase(Base):

    @classmethod
    def setUpClass(cls):              
        cls.projectName = '项目' + Base.now
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.project_button()
        cls.page = ProjectSearchPage(cls.driver) 
        cls.page.projectSearch_iframe_in()

    #用例：修改项目详情，依赖用例03‘添加项目’
    def test_admin_01_project_modify(self):		
        self.page.projectName_text(self.projectName)
        self.page.search_button()
        try:
            self.page.detail_button()
        except:
            self.write_log('error', '项目不存在')
        self.page.projectNo_text('-MODIFY')
        self.page.indi_button()
        self.write_log('info', '用例5-修改项目详情完成')

            
    #用例：项目个性化配置，依赖用例03‘项目查找’
    def test_admin_02_project_indi(self):
        self.page = ProjectIndiPage(self.driver)        
        self.page.client_text('客户名称')
        self.page.cash_button()
        self.page.Alipay_button()
        self.page.needService_button()   
        self.admin_project_setTemplate()
        self.admin_project_setLinkman()
        self.admin_project_setSubBC()
        self.admin_project_setPush()        
        self.admin_project_setApplicate()
        self.admin_project_setCost()        
        self.admin_project_setData()        
        self.admin_project_setExpress()           
        self.admin_project_setFile()
        self.page.submit_button()
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例5-项目个性化配置完成')
        self.sleep(1)


    @classmethod
    def tearDownClass(cls):
        cls.page.projectSearch_iframe_out()
        cls.page.close_button()

    #默认经办人配置
    def admin_project_setLinkman(self):    
        page = ProjectSetLinkmanPage(self.driver)
        page.setLinkman_button()
        page.renewalType_button()
        page.unlockType_button()
        page.identity_text('330502199409010317')
        page.name_text('默认经办人')
        page.phone_text('15626480142')
        page.email_text('1379668375@qq.com')
        page.address_text('默认经办人地址')
        page.linkmanSubmit_button()

    #所属子业务中心
    def admin_project_setSubBC(self):
        page = ProjectSetSubBCPage(self.driver)
        page.setSubBC_button()
        page.subBCName_text('自动化测试业务中心')
        page.subBCSubmit_button()

    #推送
    def admin_project_setPush(self):
        page = ProjectSetPushPage(self.driver)
        page.setLDAP_button()
        page.LDAPIp_text('192.168.0.168')
        page.LDAPPort_text('8389')
        page.LDAPLogin_text('cn=localtest')
        page.LDAPPassword_text('12345678')
        page.LDAPSubmit_button()
        page.LDAP_check()

    #模板
    def admin_project_setTemplate(self):
        page = ProjectSetTemplatePage(self.driver)
        page.setTemplate_button()
        page.templateName_text('管理系统自动化测试模板')
        page.templateSubmit_button()
        
    #应用
    def admin_project_setApplicate(self):
        page = ProjectSetApplicatPage(self.driver)
        page.setApplicat_button()
        page.template_select('管理系统自动化测试模板')
        page.applicetFee_text('10')
        page.applicatSubmit_button()

    #服务费
    def admin_project_setCost(self):
        page = ProjectSetCostPage(self.driver)
        page.setCost_button()
        page.certFee_text('10')
        page.costSubmit_button()

    #快递
    def admin_project_setExpress(self):
        page = ProjectSetExpressPage(self.driver)
        page.setExpress_button()
        page.expressFee0_button()
        page.expressFee1_button()
        page.expressFee2_button()
        page.needCert_button()
        page.expressSubmit_button()

    #有效期
    def admin_project_setData(self):
        self.sleep()
        page = ProjectSetDataPage(self.driver)
        page.setData_button()        
        page.data2_button()
        page.fixMonth_text('12')
        page.dataSubmit_button()     

    #附件
    def admin_project_setFile(self):
        page = ProjectSetFilePage(self.driver)
        page.setFile_button()
        page.fileName_text('必传附件')
        page.fileRequired_check()
        page.fileSubmit_button() 







