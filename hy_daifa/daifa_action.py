from hy_daifa.daifa_page import DaifaPage
from hy_login.untils import DriverUntil


class DaifaAction:

    def __init__(self):
        self.daifa_page = DaifaPage()

    def switch_iframe1(self):
        DriverUntil.get_driver().switch_to.frame(self.daifa_page.get_iframe1())

    def click_d_service(self):
        self.daifa_page.get_d_service().click()

    def switch_iframe2(self):
        DriverUntil.get_driver().switch_to.frame(self.daifa_page.get_d_iframe2())

    def click_order_info(self):
        self.daifa_page.get_order_info().click()

    def click_order_info_select(self):
        self.daifa_page.get_order_info_select().click()

    def click_order_confirm(self):
        self.daifa_page.get_order_confirm().click()

    def click_daifa_type(self):
        self.daifa_page.get_daifa_type().click()

    def click_luodi_company_select(self):
        self.daifa_page.get_luodi_company_select().click()

    def click_luodi_company_confirm(self):
        self.daifa_page.get_luodi_company_confirm().click()

    def click_luodi_company_type_select(self):
        self.daifa_page.get_luodi_company_type_select().click()

    def click_luodi_type(self):
        self.daifa_page.get_luodi_type().click()

    def input_daifa_count(self, count):
        self.daifa_page.get_daifa_count().send_keys(count)

    def input_daifa_money(self, money):
        self.daifa_page.get_daifa_money().send_keys(money)

    def input_daifa_code(self, code):
        self.daifa_page.get_daifa_code().send_keys(code)

    def input_daifa_pwd(self, pwd):
        self.daifa_page.get_daifa_pwd().send_keys(pwd)

    def input_up_load_01(self, ur01):
        self.daifa_page.get_up_load_01().send_keys(ur01)

    def input_up_load_02(self, ur01):
        self.daifa_page.get_up_load_02().send_keys(ur01)

    def click_submit_btn(self):
        self.daifa_page.get_submit_btn().click()