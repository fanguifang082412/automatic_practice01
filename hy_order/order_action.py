from hy_login.untils import DriverUntil
from hy_order.order_page import OrderPage


class OrderAction:
    def __init__(self):
        self.order_page = OrderPage()

    def click_order_manage(self):
        self.order_page.get_order_manage().click()

    def switch_iframe1(self):
        DriverUntil.get_driver().switch_to.frame(self.order_page.get_iframe1())

    def click_add_order_btn(self):
        self.order_page.get_add_order_btn().click()

    def switch_iframe2(self):
        DriverUntil.get_driver().switch_to.frame(self.order_page.get_iframe2())

    def input_project_name(self, project_name):
        self.order_page.get_project_name().send_keys(project_name)

    def input_order_name(self, order_name):
        self.order_page.get_order_name().send_keys(order_name)

    def input_order_type(self, order_type):
        self.order_page.get_order_type().send_keys(order_type)

    def input_service_text(self, service_text):
        self.order_page.get_service_text().send_keys(service_text)

    def input_service_condition(self, service_condition):
        self.order_page.get_service_condition().send_keys(service_condition)

    def click_service_time_select(self):
        self.order_page.get_service_time_select().click()

    def input_start_time(self):
        self.order_page.get_start_time().click()

    def click_end_time_select(self):
        self.order_page.get_end_time_select().click()

    def input_end_time(self):
        self.order_page.get_end_time().click()

    def input_people_count(self, people_count):
        self.order_page.get_people_count().send_keys(people_count)

    def input_project_money(self, prt_money):
        self.order_page.get_project_money().send_keys(prt_money)

    def click_people_load_btn(self):
        self.order_page.get_people_load_btn().click()

    def switch_iframe3(self):
        DriverUntil.get_driver().switch_to.frame(self.order_page.get_iframe3())

    def click_people_all_select(self):
        self.order_page.get_people_all_select().click()

    def switch_to_default_iframe(self):
        DriverUntil.get_driver().switch_to.parent_frame()

    def click_people_select_confirm_btn(self):
        self.order_page.get_people_select_confirm_btn().click()

    def input_attach(self, ur):
        self.order_page.get_attach_load().send_keys(ur)

    def click_submit_btn(self):
        self.order_page.get_submit_btn().click()