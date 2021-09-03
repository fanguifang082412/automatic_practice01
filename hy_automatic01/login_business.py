import time

from hy_automatic01 import login_action


class LoginBusiniss:

    def __init__(self):

        self.actionlogin = login_action.ActionLogin()

    def login_demo(self, username, password, code):
        self.actionlogin.input_username(username)
        self.actionlogin.input_pwd(password)
        self.actionlogin.input_code(code)
        time.sleep(2)
        self.actionlogin.click_login_btn()
