import platform
from base import Base
from page.cert_search_page import SearchPage
from page.cert_searchDetail_page import SearchDetailPage
from page.cert_menu_page import MenuPage

class SearchCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.page = MenuPage(cls.driver) #初始化
        cls.page.search_button()
        cls.page = SearchPage(cls.driver)
        cls.page.search_frame_in()
        cls.template = Base.template

    #用例：业务查询导出
    def test_cert_01_search(self):    
        self.page.searchBusiness_button()
        self.sleep()
        self.page.parentBC_text(Base.parentBusinessCenterName)
        self.page.project_text(Base.project)
        self.page.template_text(Base.template)
        self.page.searchCert_button()
        self.sleep(2)
        if '个人' in self.template:
            self.page.certType_select('个人证书')
        elif '单位' in self.template:
            self.page.certType_select('机构证书')
        elif '员工' in self.template:
            self.page.certType_select('机构员工证书')
        if '个人' not in self.template:        
            self.page.result_button()        
            self.sleep(2)
            self.page.allResult_button()
            self.page.moveRResult_button() 
        self.page.exportExcel_button()
  
        self.write_log('info', '用例6-业务查询完成')  
    
    #用例：业务详情
    def test_cert_02_detail(self):
        self.page.searchUser_button()
        self.sleep(2)
        self.page.userName_text('修改后用户名称'+ Base.now)        
        self.page.searchLinkman_button()
        self.sleep(2)
        self.page.linkmanName_text('经办人')         
        self.page.search_button()
        self.sleep()
        self.page.more_button()
        self.page = SearchDetailPage(self.driver)
        self.page.certInfo_button()
        self.sleep()
        self.page.download_button()
        self.page.exe('download.exe ' + Base.win + ' 修改后用户名称-签名证书') #下载证书 
        self.page.uploadFile(Base.win, 'untitled.png')  
        self.screenshot('业务查询详情')
        self.page.return_button()
        self.write_log('info', '用例6-查看业务详情完成')  

    #用例：迁移业务中心
    def tst_cert_03_moveBC(self):   
        self.page.dataMove_button()
        self.page.bc_text(Base.subBusinessCenterName)
        self.page.selectReq_button()
        self.page.moveSelected_button()
        self.page.submit_button() #确定
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例6-迁移业务中心完成')
        self.page.sleep()
        
    #用例：迁移项目
    def tst_cert_04_moveProj(self):
        self.page.searchBusiness_button()
        self.sleep()
        self.page.parentBC_text(Base.subBusinessCenterName)
        self.page.search_button()
        self.page.moveProj_radio()
        self.page.moveProj_text('项目迁移测试项目')
        self.page.moveTemp_text(Base.template)
        self.page.moveBC_text(Base.parentBusinessCenterName)
        self.page.moveProj_button() #迁移全部
        self.page.moveProjSubmit_button() #确定
        self.assertIn('成功', self.page.alert())
        self.write_log('info', '用例6-迁移项目完成')
        self.page.sleep()

    #用例：业务导出
    def test_cert_05_export(self):
        self.page.downloadExcel_button()
        self.sleep(2)
        self.page.exe('download.exe ' + Base.win + ' 业务导出')          
        self.write_log('info', '用例6-业务导出完成')

    @classmethod
    def tearDownClass(cls):
        cls.page.search_frame_out()
        cls.page.close_button()
