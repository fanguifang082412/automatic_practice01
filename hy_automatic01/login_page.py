import selenium
from selenium.webdriver.common.by import By
from hy_automatic01.base import PageBase
from hy_automatic01.untils import DriverUntil


class LoginPage(PageBase):
    def __init__(self):
        self.username = (By.CSS_SELECTOR, "#LAY-user-login-username")
        self.password = (By.CSS_SELECTOR, "#LAY-user-login-password")
        self.code = (By.CSS_SELECTOR, "#LAY-user-login-vercode")
        self.login_btn = (By.CSS_SELECTOR, "#LAY-user-login > div > div.layadmin-user-login-box.layadmin-user-login-body.layui-form > div:nth-child(5) > button")

    def find_username(self):
        self.find_element(self.username).clear()
        return self.find_element(self.username)

    def find_pwd(self):
        self.find_element(self.password).clear()
        return self.find_element(self.password)

    def find_xcode(self):
        self.find_element(self.code).clear()
        return self.find_element(self.code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)