import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_infoRegister_page import InfoRegisterPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_menu_page import MenuPage
from page.cert_infoExport_page import InfoExportPage

'''
脚本信息：业务信息登记用例
编写人：郭丹颖
编写时间：2020-4-1
'''
class InfoRegisterCase(Base):
    
    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver)     
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.InfoPage = InfoPage(cls.driver)  
        cls.InfoRegisterPage = InfoRegisterPage(cls.driver)      
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)
        cls.InfoExportPage = InfoExportPage(cls.driver)

    #用例：证书申请-业务登记
    def tst_cert_InfoRegister_01(self):
        self.MenuPage.business_button()
        self.BusinessPage.business_frame_in()        
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.infoRegProject, Base.infoRegtemplate, '业务信息登记回归' + Base.now)
        self.InfoPage.YNID_text('云南电力交易系统用户ID')
        self.InfoPage.YNAccount_text('云南电力交易系统账号')
        #self.InfoPage.certLX_text('003')

        '''登记业务信息'''
        self.InfoRegisterPage.customId_text('用户ID')
        self.InfoRegisterPage.tradeOrgName_text('电力交易系统单位名称')
        self.InfoRegisterPage.tradeAccount_text('电力交易系统账号')
        self.InfoRegisterPage.certApplyDate_button()
        self.InfoRegisterPage.dateSubmit()
        self.InfoRegisterPage.receiveDate_button()
        self.InfoRegisterPage.dateSubmit()

        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(False) 
        self.sleep(2)       
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例12-证书申请业务登记完成')   
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()

    #用例：证书变更-业务登记
    def tst_cert_InfoRegister_02(self):
        self.BusinessPage.acceptBusiness('证书变更', 1)
        self.InfoPage.getInfo(Base.infoRegtemplate)

        '''登记变更的业务信息'''
        self.InfoRegisterPage.bindChangeDate_button()
        self.InfoRegisterPage.dateSubmit()
        self.InfoRegisterPage.registrationProjectMemo_text('备注')
        self.InfoRegisterPage.bindChangeReason_text('系统账号绑定变更理由')
        self.InfoRegisterPage.unbindChangeDate_button()
        self.InfoRegisterPage.dateSubmit()

        self.InfoPage.submit_button()
        self.CheckPage.checkBusiness(True)
        self.assertIn('成功', self.CheckResultPage.tip_text())
        self.write_log('info', '用例12-证书变更业务登记完成')   
        self.BusinessPage.business_frame_out() 
        self.BusinessPage.close_button() 

    #用例：业务登记信息导出
    def test_cert_InfoRegister_03(self):
        self.MenuPage.infoExport_button()
        self.InfoExportPage.InfoExp_frame_in()    
        self.InfoExportPage.project_text(Base.infoRegProject)
        self.InfoExportPage.export_button()
        self.sleep(4)
        self.InfoExportPage.downloadExcel_button()
        self.sleep()
        self.InfoExportPage.exe('download.exe ' + Base.win + ' 业务登记信息导出')
        self.InfoExportPage.InfoExp_frame_out() 
        self.InfoExportPage.close_button() 

    @classmethod
    def tearDownClass(cls):
        cls.MenuPage.deleteCert()
    
