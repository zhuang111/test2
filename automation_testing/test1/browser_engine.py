from selenium import webdriver
import configparser
import os


class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome
    """
    dir = os.path.dirname(os.path.abspath('.'))
    print("Current path "+dir)
    config_path = dir+"\\config\\config.ini"
    config = configparser.ConfigParser()

    config.read(config_path)

    browser_type = config.get("BrowserType","BrowserName")
    # browser_type = "Chrome"

    # def __init__(self,driver):
    #     self.driver = driver

    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """
        if self.browser_type == "Chrome":
            self.driver = webdriver.Chrome()
        elif self.browser_type == "IE":
            self.driver = webdriver.Ie()
        elif self.browser_type == "Firefox":
            self.driver = webdriver.Firefox()
        else:self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        return self.driver

    def find_element(self, arrAttri):
        if arrAttri[0] == "xPath":
            element = self.driver.find_element_by_xpath(arrAttri[1])

        elif arrAttri[0] == 'id':
            element = self.driver.find_element_by_id(arrAttri[1])
        elif arrAttri[0] == "name":
            element = self.driver.find_element_by_name(arrAttri[1])

        return element
# browser = BrowserEngine()
# browser.get_browser()
