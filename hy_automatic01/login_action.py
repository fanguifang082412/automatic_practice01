import time

from hy_automatic01 import base, login_page
from hy_automatic01.base import ActionBase



class ActionLogin(ActionBase):

    def __init__(self):
        self.login_ele = login_page.LoginPage()

    def input_username(self, username):
        # self.login_ele.find_username().send_keys(username)
        self.input_text(self.login_ele.find_username(),username)

    def input_pwd(self, password):
        # self.login_ele.find_pwd().send_keys(password)
        self.input_text(self.login_ele.find_pwd(), password)

    def input_code(self, code):
        # self.login_ele.find_xcode().send_keys(code)
        self.input_text(self.login_ele.find_xcode(), code)

    def click_login_btn(self):
        self.login_ele.find_login_btn().click()