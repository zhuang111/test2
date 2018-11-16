# coding=utf-8
from framework.utils.base_page import BasePage
from objects.enovia import login_obj


class HomePage(BasePage,login_obj):
    # input_box = "id=>kw"
    # search_submit_btn = "xpath=>//*[@id='su']"
    # # 百度新闻入口
    # news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"

    def login(self, username, password):
        #input username
        self.type(self.usernamebox, username)
        #input password
        self.type(self.passwordbox,password)
        self.click(self.login_btn)

