import time

from hy_login.untils import DriverUntil
from hy_order_check.check_action import CheckAction


class CheckBusiness:

    def __init__(self):
        self.check_action = CheckAction()

    def order_check_01(self, check_info, code, pwd):
        self.check_action.click_order_list()
        self.check_action.switch_iframe1()
        if self.check_action.get_status() == "待审核":
            self.check_action.click_order_check1()
            self.check_action.switch_iframe2()
            js = "window.scrollTo(0, 1000)"
            DriverUntil.get_driver().execute_script(js)
            self.check_action.input_check_info(check_info)
            self.check_action.input_check_code(code)
            self.check_action.input_check_pwd(pwd)
            self.check_action.click_check_pass_select()
            self.check_action.click_check_submit_btn()
            # self.check_action.move_to_yunying_account()
            # time.sleep(5)
            # self.check_action.click_exit()
            # time.sleep(5)
            # self.check_action.click_exit_account()

        else:
            print("没有可审核的订单")


    def order_check_02(self, check_info_02, code_02, pwd_02):
        self.check_action.click_order_list2()
        self.check_action.switch_iframe1_2()
        if self.check_action.get_status_2() == "订单二审":
            self.check_action.click_order_check2()
            self.check_action.switch_iframe2_2()
            js = "window.scrollTo(0, 1000)"
            DriverUntil.get_driver().execute_script(js)
            self.check_action.input_check_info_2(check_info_02)
            self.check_action.input_check_code_2(code_02)
            self.check_action.input_check_pwd_2(pwd_02)
            self.check_action.click_check_pass_select_2()
            self.check_action.click_check_submit_btn_2()
            # self.check_action.move_to_yunying_account_2()
            # time.sleep(5)
            # self.check_action.click_exit_2()
            # time.sleep(5)
            # self.check_action.click_exit_account()

        else:
            print("没有可审核的订单")