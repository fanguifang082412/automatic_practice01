from hy_login import base
from hy_login.login_page import LoginPage





class ActionLogin(base.ActionBase):

    def __init__(self):
        self.login_ele = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_ele.find_username(), username)
        # self.login_ele.find_username().send_keys(username)

    def input_pwd(self, password):
        self.input_text(self.login_ele.find_pwd(), password)
        # self.login_ele.find_pwd().send_keys(password)

    def input_code(self, code):
        self.input_text(self.login_ele.find_xcode(), code)
        # self.login_ele.find_xcode().send_keys(code)

    def click_login_btn(self):
        self.login_ele.login_btn().click()

