from test1.basepage import BasePage
from test1.browser_engine import BrowserEngine
import time

Browser = BrowserEngine()
browser = Browser.get_browser()
    # Page = BasePage(Browser.get_browser)
    # def setUp(self):
        # Browser = BrowserEngine()
        # browser = self.Browser.get_browser()

        # Page = BasePage(browser)
        # self.Page.open_url("https://plmtest.pg.com")
browser.get("https://plmtest.pg.com")


     # browser.find_element_by_name("username").send_keys("dsotest27.im")
element_username = Browser.find_element(["name", "username"])
element_username.send_keys("dsotest27.im")

element_password = Browser.find_element(["name","password"])
element_password.send_keys("Check789")

element_login_btn = Browser.find_element(["xPath","//input[@type = 'submit']"])
element_login_btn.click()



