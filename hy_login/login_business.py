import time
from hy_login.login_action import ActionLogin


class LoginBusiniss:

    def __init__(self):

        self.action_login = ActionLogin()

    def login(self, username, password, code):
        self.action_login.input_username(username)
        self.action_login.input_pwd(password)
        self.action_login.input_code(code)
        time.sleep(2)
        self.action_login.click_login_btn()



