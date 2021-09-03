from hy_login.untils import DriverUntil
from hy_recharge.recharge_page import RechageDemo


class RechageAction:

    def __init__(self):
        self.recharge_demo = RechageDemo()

    # def click_company_home(self):
    #     self.recharge_demo.get_company_home().click()

    def switch_iframe1(self):
        iframe1 = self.recharge_demo.get_iframe1()
        DriverUntil.get_driver().switch_to.frame(iframe1)

    def click_recharge(self):
        self.recharge_demo.get_recharge().click()

    def click_recharge_company_select(self):
        self.recharge_demo.get_recharge_company_select().click()

    def click_recharge_company(self):
        self.recharge_demo.get_recharge_company().click()

    def switch_iframe2(self):
        iframe2 = self.recharge_demo.get_iframe2()
        DriverUntil.get_driver().switch_to.frame(iframe2)

    def input_money(self, money):
        self.recharge_demo.get_recharge_money().send_keys(money)

    def click_image_upload(self, ur):
        self.recharge_demo.find_image_upload().send_keys(ur)

    def submit_btn(self):
        self.recharge_demo.get_recharge_submit().click()



