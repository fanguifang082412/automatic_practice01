import time
from hy_login.untils import DriverUntil
from hy_order.order_action import OrderAction



class OrderBusiness:
    def __init__(self):
        self.order_action = OrderAction()

    def add_order(self, project_name, order_name, order_type, service_text, service_condition, people_count, prt_money):
        time.sleep(5)
        self.order_action.click_order_manage()
        self.order_action.switch_iframe1()
        self.order_action.click_add_order_btn()
        self.order_action.switch_iframe2()
        self.order_action.input_project_name(project_name)
        self.order_action.input_order_name(order_name)
        self.order_action.input_order_type(order_type)
        self.order_action.input_service_text(service_text)
        self.order_action.input_service_condition(service_condition)
        self.order_action.click_service_time_select()
        self.order_action.input_start_time()
        self.order_action.click_end_time_select()
        self.order_action.input_end_time()
        self.order_action.input_people_count(people_count)
        self.order_action.input_project_money(prt_money)
        self.order_action.click_people_load_btn()
        self.order_action.switch_iframe3()
        self.order_action.click_people_all_select()
        self.order_action.switch_to_default_iframe()
        self.order_action.click_people_select_confirm_btn()
        # self.order_action.input_attach(ur)
        self.order_action.click_submit_btn()

