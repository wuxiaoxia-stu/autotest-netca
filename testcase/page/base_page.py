
import os, time, random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#基本层

class BasePage(object):
  
    def __init__(self, driver):
        self.driver = driver           

    '''最大化浏览器，打开url'''
    def open(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    '''获取元素，会等待30秒钟至元素出现'''
    def element(self, *loc):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(loc))        
        return element

    def element5s(self, *loc):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located(loc))
        return element

    #判断元素是否含有属性attribute,值value
    def attribute_exist(self, *loc,attribute,value):
        try :
            val = self.element(*loc).get_attribute(attribute)
            if val == value:
                return True
            return False
        except:
            return False

    def iframe_in(self, iframeid):
        return self.driver.switch_to.frame(iframeid)


    def iframe_out(self):
        return self.driver.switch_to.default_content()

    #确认弹窗并返回弹窗内容
    def alert(self):
        i = 1
        while True:
            if i > 20:
                raise Exception('没有弹窗')
            try:
                alert = self.driver.switch_to_alert()  
                text = alert.text
            except:
                time.sleep(1)
                i = i + 1
            else:                
                alert.accept()
                break
        return text

    #取消弹窗
    def dismiss(self):
        alert = self.driver.switch_to_alert()
        text = alert.text
        alert.dismiss()
        time.sleep(1)
        return text

    '''运行exe'''
    def exe(self, exename):
        path = os.getcwd()
        os.chdir(path + '\\other\\exe')
        os.system(exename)
        time.sleep(1)
        os.chdir(path)

    '''多选框'''
    def li(self, text):
        xpath = "//li[contains(text(),'" + text + "')]"
        return self.element(By.XPATH, xpath)

    #先清空，再赋值
    def send_keys(self, *loc, text):
        element = self.element(*loc)
        element.clear()
        element.send_keys(text)

    '''如果按钮未被选中，则选中'''
    def check(self, *loc):
        element = self.element(*loc)
        if not element.is_selected():
            element.click()

    #文本框，元素不出现跳过
    def input(self, *loc, text):
        try:
            self.driver.find_element(*loc).clear()
            self.driver.find_element(*loc).send_keys(text)
        except:
            pass

    #单选框，元素不出现跳过
    def clickbutton(self,*loc):
        try:
            self.driver.find_element(*loc).click()
        except:
            pass

    '''下拉框'''
    def select(self, *loc, text):
        try:
            sel = Select(self.driver.find_element(*loc))
            sel.select_by_visible_text(text)
        except:
            pass

    #切换到新打开的窗口
    def to_new_window(self,old_window):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != old_window:
                self.driver.switch_to_window(handle)
                self.driver.maximize_window()
                
    #切换到旧的窗口
    def to_old_window(self,old_window):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle == old_window:
                self.driver.switch_to_window(handle)

    def closeIE(self):
        self.driver.close()

    #鼠标双击
    def double_click(self, *loc):
        element = self.element(*loc)
        ActionChains(self.driver).double_click(element).perform()

    #返回元素文本内容
    def text(self, *loc):
        return self.element(*loc).text

    '''等待'''
    def sleep(self, t=1):
        time.sleep(t)

    #获取当前URL
    def getURL(self):
        return self.driver.current_url