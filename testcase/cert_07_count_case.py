
import random
from base import Base
from page.cert_count_page import CountPage
from page.cert_menu_page import MenuPage

class CountCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.count_button()
        cls.page = CountPage(cls.driver)
        cls.page.count_frame_in()       
        cls.project = Base.project
       
    #用例：有效证书量统计
    def test_cert_01_valid(self):
        self.page.count_button()
        self.page.project_select(self.project)
        self.page.moveProj_button()
        self.page.time_button()
        self.page.time_frame_in()
        self.page.today_button()
        self.page.time_frame_out()
        self.page.submit_button()
        self.screenshot('有效证书量统计')
        self.page.export_button()
        self.sleep()
        self.page.exe('download.exe ' +  Base.win + ' 有效证书量统计')
        self.write_log('info', '用例1-有效证书量统计查询导出完成') 
        

    #用例：过期证书量统计
    def test_cert_02_expire(self):
        self.page.expire_button()
        self.page.expireTimeStart_button()
        self.page.time_frame_in()
        self.page.today_button()
        self.page.time_frame_out()
        self.page.oneYear_button()
        self.page.submit_button()
        self.screenshot('到期证书量统计')
        self.page.export_button()
        self.sleep()
        self.page.exe('download.exe ' +  Base.win + ' 到期证书量统计')
        self.write_log('info', '用例2-过期证书量统计查询导出完成') 

    #用例：证书业务量统计
    def test_cert_03_business(self):
        self.page.business_button()
        self.page.BC_select(Base.parentBusinessCenterName)
        self.page.moveBC_button()
        self.page.allBusi_button()
        self.page.moveBusi_button()
        self.page.busiTimeStart_button()
        self.page.time_frame_in()
        self.page.one_button()
        self.page.busiTimeSubmit_button()
        self.page.time_frame_out()        
        self.page.busiTimeEnd_button()
        self.page.time_frame_in()
        self.page.today_button()
        self.page.time_frame_out()
        self.page.submit_button()
        self.screenshot('证书业务量统计')
        self.page.export_button()
        self.sleep(2)
        self.page.exe('download.exe ' +  Base.win + ' 证书业务量统计')
        self.write_log('info', '用例3-证书业务量统计查询导出完成') 
    
    #用例：发票汇总表统计
    def test_cert_04_invoiceSummary(self):
        self.page.invoiceCount_button()
        self.page.invoiveCSubmit_button()
        self.screenshot('发票汇总表统计')
        self.write_log('info', '用例4-发票汇总表统计查询完成')


    #用例：发票明细表统计
    def test_cert_05_invoiceDetail(self):
        self.page.invoiceDetail_button()
        self.page.invoiveCSubmit_button()
        self.screenshot('发票明细表统计')
        self.page.invoiveExport_button()
        self.sleep(2)
        self.page.exe('download.exe ' +  Base.win + ' 发票统计')
        self.write_log('info', '用例5-发票明细表统计查询完成')
        self.page.count_frame_out()
        self.page.close_button()
        self.page = MenuPage(self.driver)
        self.page.count_button()
        self.page = CountPage(self.driver)
        self.page.count_frame_in()                 

    #用例：工作量统计
    def test_cert_06_workload(self):
        self.page.project_select(self.project)
        self.page.moveProj_button()
        self.page.invoiveCSubmit_button()
        self.sleep(8)
        self.screenshot('工作量统计')
        self.page.workloadExport_button()
        self.sleep(6)
        self.page.exe('download.exe ' +  Base.win + ' 工作量统计')
        self.write_log('info', '用例6-工作量统计查询导出完成')         

    @classmethod
    def tearDownClass(cls):
        cls.page.count_frame_out()
        cls.page.close_button()
