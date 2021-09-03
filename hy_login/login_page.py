from selenium.webdriver.common.by import By
from hy_login import base



class LoginPage(base.PageBase):

    def __init__(self):
        self.username = (By.CSS_SELECTOR, "#LAY-user-login-username")
        self.password = (By.CSS_SELECTOR, "#LAY-user-login-password")
        self.code = (By.CSS_SELECTOR, "#LAY-user-login-vercode")
        self.login = (By.CSS_SELECTOR, "#LAY-user-login > div > div.layadmin-user-login-box.layadmin-user-login-body.layui-form > div:nth-child(5) > button")

    def find_username(self):
        self.find_element(self.username).clear()
        return self.find_element(self.username)
        # DriverUntil.get_driver().find_element(*self.username).clear()

    def find_pwd(self):
        self.find_element(self.password).clear()
        return self.find_element(self.password)
        # DriverUntil.get_driver().find_element(*self.password).clear()
        # return DriverUntil.get_driver().find_element(*self.password)

    def find_xcode(self):
        self.find_element(self.code).clear()
        return self.find_element(self.code)
        # DriverUntil.get_driver().find_element(*self.code).clear()
        # return DriverUntil.get_driver().find_element(*self.code)

    def login_btn(self):
        return self.find_element(self.login)
        # return DriverUntil.get_driver().find_element(*self.login)


