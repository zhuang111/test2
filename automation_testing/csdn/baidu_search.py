from selenium import webdriver
import time
from test1.basepage import BasePage


class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    basepage = BasePage(driver)

    def open_baidu(self):
        """
        打开百度首页
        :return:
        """
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(5)

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(1)

        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
