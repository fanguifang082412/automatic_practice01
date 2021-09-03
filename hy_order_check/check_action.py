from hy_login.untils import DriverUntil
from hy_order_check.check_page import CheckOrderPage
from selenium.webdriver import ActionChains


class CheckAction:

    #对账号运营一页面元素进行操作
    def __init__(self):
        self.check_order_page = CheckOrderPage()

    def click_order_list(self):
        self.check_order_page.get_order_list().click()

    def switch_iframe1(self):
        DriverUntil.get_driver().switch_to.frame(self.check_order_page.get_iframe1())

    def get_status(self):
        return self.check_order_page.get_order_status().text

    def click_order_check1(self):
        self.check_order_page.get_order_check1().click()

    def switch_iframe2(self):
        DriverUntil.get_driver().switch_to.frame(self.check_order_page.get_iframe2())

    def input_check_info(self, check_info):
        self.check_order_page.get_check_info().send_keys(check_info)

    def input_check_code(self, code):
        self.check_order_page.get_check_code().send_keys(code)

    def input_check_pwd(self, pwd):
        self.check_order_page.get_check_pwd().send_keys(pwd)

    def click_check_pass_select(self):
        self.check_order_page.get_check_pass_select().click()

    def click_check_submit_btn(self):
        self.check_order_page.get_check_submit_btn().click()

    def move_to_yunying_account(self):
        ActionChains(DriverUntil.get_driver()).move_to_element(self.check_order_page.get_yunying_account()).perform()

    def click_exit(self):
        self.check_order_page.get_exit().click()


    # 对账号运营二页面元素进行操作
    def click_order_list2(self):
        self.check_order_page.get_order_list2().click()

    def switch_iframe1_2(self):
        DriverUntil.get_driver().switch_to.frame(self.check_order_page.get_iframe1_2())

    def get_status_2(self):
        return self.check_order_page.get_order_status_2().text

    def click_order_check2(self):
        self.check_order_page.get_order_check2().click()

    def switch_iframe2_2(self):
        DriverUntil.get_driver().switch_to.frame(self.check_order_page.get_iframe2_2())

    def input_check_info_2(self, check_info):
        self.check_order_page.get_check_info_2().send_keys(check_info)

    def input_check_code_2(self, code):
        self.check_order_page.get_check_code_2().send_keys(code)

    def input_check_pwd_2(self, pwd):
        self.check_order_page.get_check_pwd_2().send_keys(pwd)

    def click_check_pass_select_2(self):
        self.check_order_page.get_check_pass_select_2().click()

    def click_check_submit_btn_2(self):
        self.check_order_page.get_check_submit_btn_2().click()

    def move_to_yunying_account_2(self):
        ActionChains(DriverUntil.get_driver()).move_to_element(self.check_order_page.get_yunying_account_2()).perform()

    def click_exit_2(self):
        self.check_order_page.get_exit_2().click()
