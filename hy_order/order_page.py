import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from hy_login.untils import DriverUntil



class OrderPage:

    def __init__(self):
        self.order_manage = (By.PARTIAL_LINK_TEXT, "订单管理")
        self.iframe1 = (By.XPATH, '//iframe[@src="/company/Order/index"]')
        self.add_order_btn = (By.XPATH, '//button[contains(text(),"新增订单")]')
        self.iframe2 = (By.XPATH, '//iframe[@allowtransparency="true" and @src="/company/order/save.html"]')
        self.project_name = (By.XPATH, '//input[@name="project_name"]')
        self.order_name = (By.XPATH, '//input[@name="order_name"]')
        self.order_type = (By.XPATH, '//input[@name="business_type"]')
        self.service_text = (By.XPATH, '/html/body/div/div/div/div/form/div[4]/div/div/textarea')
        self.service_condition = (By.XPATH, '/html/body/div/div/div/div/form/div[5]/div/div/textarea')
        self.service_time_select = (By.XPATH, '//*[@id="start"]')
        self.start_time = (By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div/span[2]')
        self.end_time_select = (By.XPATH, '//*[@id="end"]')
        self.end_time = (By.XPATH, '//*[@id="layui-laydate2"]/div[2]/div/span[2]')
        self.people_count = (By.XPATH, '/html/body/div/div/div/div/form/div[7]/div/div/input')
        self.project_money = (By.XPATH, '/html/body/div/div/div/div/form/div[8]/div/div/input')
        self.people_load_btn = (By.XPATH, '/html/body/div/div/div/div/form/div[9]/div/div/button')
        self.iframe3 = (By.XPATH, '//*[@id="layui-layer-iframe1" and @src="/company/order/select_personnel.html"]')
        self.people_all_select = (By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[1]/table/thead/tr/th[1]/div/div/i')
        self.people_select_confirm_btn = (By.XPATH, '//a[contains(text(), "确定")]')
        self.submit_btn = (By.XPATH, '/html/body/div[1]/div/div/div/form/div[12]/div/button[1]')
        self.attach_load = (By.XPATH, '//*[@id="fujianhet"]/div/div/input')


    def get_order_manage(self):
        order_manage = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_manage))
        return order_manage
        # return DriverUntil.get_driver().find_element(*self.order_manage)

    def get_iframe1(self):
        iframe1_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe1))
        return iframe1_ele

    def get_add_order_btn(self):
        add_order_btn = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.add_order_btn))
        return add_order_btn
        # return DriverUntil.get_driver().find_element(*self.add_order_btn)

    def get_iframe2(self):
        return DriverUntil.get_driver().find_element(*self.iframe2)

    def get_project_name(self):
        return DriverUntil.get_driver().find_element(*self.project_name)

    def get_order_name(self):
        return DriverUntil.get_driver().find_element(*self.order_name)

    def get_order_type(self):
        return DriverUntil.get_driver().find_element(*self.order_type)

    def get_service_text(self):
        return DriverUntil.get_driver().find_element(*self.service_text)

    def get_service_condition(self):
        return DriverUntil.get_driver().find_element(*self.service_condition)

    def get_service_time_select(self):
        return DriverUntil.get_driver().find_element(*self.service_time_select)

    def get_start_time(self):
        return DriverUntil.get_driver().find_element(*self.start_time)

    def get_end_time_select(self):
        return DriverUntil.get_driver().find_element(*self.end_time_select)

    def get_end_time(self):
        return DriverUntil.get_driver().find_element(*self.end_time)

    def get_people_count(self):
        return DriverUntil.get_driver().find_element(*self.people_count)

    def get_project_money(self):
        return DriverUntil.get_driver().find_element(*self.project_money)

    def get_people_load_btn(self):
        return DriverUntil.get_driver().find_element(*self.people_load_btn)

    def get_iframe3(self):
        iframe3_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe3))
        return iframe3_ele

    def get_people_all_select(self):
        people_select = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.people_all_select))
        return people_select
        # return DriverUntil.get_driver().find_element(*self.people_all_select)

    def get_people_select_confirm_btn(self):
        confirm_btn = WebDriverWait(DriverUntil.get_driver(), 15, poll_frequency=0.5).until(lambda x: x.find_element(*self.people_select_confirm_btn))
        return confirm_btn
        # return DriverUntil.get_driver().find_element(*self.people_select_confirm_btn)

    def get_attach_load(self):
        attach_ele = WebDriverWait(DriverUntil.get_driver(), 15, poll_frequency=0.5).until(lambda x: x.find_element(*self.attach_load))
        return attach_ele

    def get_submit_btn(self):
        return DriverUntil.get_driver().find_element(*self.submit_btn)





























