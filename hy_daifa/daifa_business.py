import time
import unittest
from hy_daifa.daifa_action import DaifaAction
from hy_login.untils import DriverUntil


class DaifaBusiness:

    def __init__(self):
        self.daifa_action = DaifaAction()

    def daifa_business(self, count, money, code, pwd, ur01, ur02):

        self.daifa_action.switch_iframe1()
        time.sleep(1)
        self.daifa_action.click_d_service()
        self.daifa_action.switch_iframe2()
        time.sleep(1)
        self.daifa_action.click_order_info()
        time.sleep(1)
        self.daifa_action.click_order_confirm()
        time.sleep(1)
        self.daifa_action.click_daifa_type()
        self.daifa_action.click_luodi_company_select()
        self.daifa_action.click_luodi_company_confirm()
        time.sleep(1)
        self.daifa_action.click_luodi_company_type_select()
        self.daifa_action.click_luodi_type()
        self.daifa_action.input_daifa_count(count)
        self.daifa_action.input_daifa_money(money)
        self.daifa_action.input_daifa_code(code)
        self.daifa_action.input_daifa_pwd(pwd)
        self.daifa_action.input_up_load_01(ur01)
        self.daifa_action.input_up_load_02(ur02)
        self.daifa_action.click_submit_btn()
