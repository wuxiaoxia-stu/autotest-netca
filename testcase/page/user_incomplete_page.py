from selenium.webdriver.common.by import By
from .base_page import BasePage

class IncompletePage(BasePage):
	pageSize_select_loc = (By.XPATH,"//select[@id='showPageSizeSelect']")
	finishOper_select_loc = (By.XPATH, "//select[@id='completeStatus']")
	search_button_loc = (By.XPATH, "//input[@value='查询']")
	title_text_loc = (By.XPATH,"//*[@id='divSelectTable']/table/caption")

	
	#每页显示记录条数
	def pageSize_select(self):
		self.select(*self.pageSize_select_loc,text="50")

	# 选择已完成操作
	def notFinishOper_select(self):
		self.select(*self.finishOper_select_loc, text="未完成")

	#选择已完成操作
	def finishOper_select(self):
		self.select(*self.finishOper_select_loc,text="已完成")
		
	#点击查询按钮
	def search_button(self):
		self.element(*self.search_button_loc).click()

	#返回标题名称
	def title_text(self):
		return self.text(*self.title_text_loc)
		
	#点击修改按钮
	def modify_button(self,business_number):
		modify_button_loc = (By.XPATH, "//a[contains(@href,'" + business_number + "') and contains(.,'修改')]")
		self.double_click(*modify_button_loc)
	
	#点击资料上传按钮
	def upFile_button(self,business_number):
		upFile_button_loc = (By.XPATH, "//a[contains(@onclick,'"+business_number+"') and contains(.,'资料上传')]") 
		self.double_click(*upFile_button_loc)
		
	#点击证书安装按钮
	def installCert_button(self,business_number):
		installCert_button_loc = (By.XPATH, "//a[contains(@onclick,'" + business_number + "') and contains(.,'证书安装')]")
		self.double_click(*installCert_button_loc)

	#点击添加按钮-多员工业务
	def addUser_button(self,business_number):
		addUser_button_loc = (By.XPATH, "//a[contains(@href,'" + business_number + "') and contains(.,'添加业务')]")
		self.double_click(*addUser_button_loc)

	#修改信息流程
	def modifyInformation(self,business_number):
		self.pageSize_select()
		self.sleep(1)
		self.modify_button(business_number)

	#添加多员工业务流程
	def addUser(self,business_number):
		self.notFinishOper_select()
		self.search_button()
		self.pageSize_select()
		self.sleep(1)
		self.addUser_button(business_number)
		self.alert()
	
	#资料上传流程
	def updateFile(self,business_number):
		self.pageSize_select()
		self.sleep(1)
		self.upFile_button(business_number)
	
	#证书安装流程
	def installCert(self,business_number):
		self.sleep(1)
		self.finishOper_select()
		self.search_button()
		self.pageSize_select()
		self.sleep(1)
		self.installCert_button(business_number)
		self.sleep(3)
		self.exe('inputpassword.exe')
		self.alert()