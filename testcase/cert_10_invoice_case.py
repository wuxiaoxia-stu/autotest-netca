
import platform, random
from base import Base
from page.cert_business_page import BusinessPage
from page.cert_info_page import InfoPage
from page.cert_check_page import CheckPage
from page.cert_checkResult_page import CheckResultPage
from page.cert_invoice_page import InvoicePage
from page.cert_express_page import ExpressPage
from page.cert_menu_page import MenuPage
from page.login_page import LoginPage

class InvoiceCase(Base):
     
    @classmethod
    def setUpClass(cls):
        cls.MenuPage = MenuPage(cls.driver) #初始化
        cls.MenuPage.business_button()
        cls.BusinessPage = BusinessPage(cls.driver)
        cls.BusinessPage.business_frame_in()
        cls.InfoPage = InfoPage(cls.driver)
        cls.CheckPage = CheckPage(cls.driver)
        cls.CheckResultPage = CheckResultPage(cls.driver)
        cls.InvoicePage = InvoicePage(cls.driver)
        cls.ExpressPage = ExpressPage(cls.driver)
    
    #用例：开电子发票
    def test_cert_01_ElectronicInvoice(self):
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '电子发票' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.cod_button()
        self.CheckPage.checkBusiness(False)

        self.CheckResultPage.newInvoice_button()
        self.InvoicePage.newEInvoice()
        self.assertIn('开具电子发票成功！', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-开电子发票完成') 

    #用例：下单打单
    def test_cert_02_express(self):
        self.CheckResultPage.express_button()
        self.ExpressPage.getExpress(Base.win)
        self.assertIn('打单成功', self.CheckResultPage.tipExpress_text())
        self.write_log('info', '用例10-下单打单完成') 

    #用例：下载电子发票
    @Base.skip_dependon(depend="test_cert_01_ElectronicInvoice")
    def test_cert_03_ElectronicInvoice(self):
        self.CheckResultPage.modifyInvoice_button()
        self.InvoicePage.downloadEInvoice(Base.win)
        self.write_log('info', '用例10-下载电子发票完成') 

    #用例：冲红电子发票
    @Base.skip_dependon(depend="test_cert_01_ElectronicInvoice")
    def test_cert_04_ElectronicInvoice(self):  
        self.InvoicePage.uninvoiceInfo_text('发票冲红备注')
        self.InvoicePage.uninvoice_button() #点击冲红
        self.InvoicePage.alert()
        self.assertIn('冲红成功', self.CheckResultPage.tipInvoice_text())       
        self.write_log('info', '用例10-冲红电子发票完成') 
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button()        
    
    #用例：开纸质发票-普票
    def test_cert_05_pupiao(self):           
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '普票' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.pupiao_check()
        self.CheckPage.checkBusiness(True)
        self.CheckResultPage.newInvoice_button()
        self.InvoicePage.newPupiao(random.randint(10000000,99999999), '012345678000', 10)
        self.assertIn('开具发票成功', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-开纸质发票-普票完成') 
    
    #用例：作废纸质发票-普票
    @Base.skip_dependon(depend="test_cert_05_pupiao")
    def test_cert_06_pupiao(self):  
        self.CheckResultPage.modifyInvoice_button()
        self.InvoicePage.pUninvoiceInfo_text('作废备注')
        self.InvoicePage.pUninvoiceSubmit_button()
        self.InvoicePage.alert()
        self.assertIn('操作成功', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-作废纸质发票-普票完成') 
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button() 

    #用例：开纸质发票-专票
    def test_cert_07_zhuanpiao(self):           
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '专票' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.zhuanpiao_check()
        self.CheckPage.checkBusiness(True)
        self.CheckResultPage.newInvoice_button()
        self.InvoicePage.newZhuanpiao(random.randint(10000000,99999999), '012345678000', 10)
        self.assertIn('开具发票成功', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-开纸质发票-专票完成') 

    #用例：冲红纸质发票-专票
    @Base.skip_dependon(depend="test_cert_07_zhuanpiao")
    def test_cert_08_zhuanpiao(self):  
        self.CheckResultPage.modifyInvoice_button()
        self.InvoicePage.pUninvoice_button()
        self.InvoicePage.pUninvoiceInfo2_text('冲红备注')
        self.InvoicePage.invoiceNoNew_text(random.randint(10000000,99999999))
        self.InvoicePage.invoiceCodeNew_text('012345678000')
        self.InvoicePage.pUninvoiceSubmit_button()
        self.InvoicePage.alert()
        self.assertIn('发票冲红成功', self.CheckResultPage.tipInvoice_text())  
        self.write_log('info', '用例10-冲红纸质发票-专票完成') 
        self.CheckResultPage.continue_button()
        self.CheckPage.back_button() 

    #用例：开纸质发票-定额
    def test_cert_09_zhuanpiao(self):           
        self.BusinessPage.acceptBusiness('证书申请')
        self.InfoPage.addInfo(Base.project, Base.template, '定额' + Base.now)
        self.InfoPage.submit_button()
        self.CheckPage.dinge_check()
        self.CheckPage.checkBusiness(True)
        self.CheckResultPage.newInvoice_button()
        self.InvoicePage.newDinge(random.randint(10000000,99999999), '012345678010')
        self.assertIn('开具发票成功', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-开纸质发票-定额完成') 

    #用例：重用纸质发票-定额
    @Base.skip_dependon(depend="test_cert_09_zhuanpiao")
    def test_cert_10_zhuanpiao(self):  
        self.CheckResultPage.modifyInvoice_button()
        self.InvoicePage.pReuseInfo_text('定额重用备注')
        self.InvoicePage.pReuse_button()             
        self.InvoicePage.alert()       
        self.assertIn('重用成功', self.CheckResultPage.tipInvoice_text())
        self.write_log('info', '用例10-重用纸质发票-定额完成') 
    
    @classmethod
    def tearDownClass(cls):
        cls.BusinessPage.business_frame_out()
        cls.BusinessPage.close_button()
        cls.MenuPage.deleteCert()

    