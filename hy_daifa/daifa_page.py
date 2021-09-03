from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from hy_login.untils import DriverUntil


class DaifaPage:

    def __init__(self):
        self.iframe1 = (By.XPATH, '//*[@id="LAY_app_body"]/div/iframe')
        self.d_service = (By.XPATH, '//*[@id="pricing"]/div/div/div[2]/div[3]/div/h3')
        self.iframe2 = (By.XPATH, '//iframe[contains(text(),layui-layer-iframe) and @scrolling="auto"]')
        self.order_info = (By.XPATH, '//*[@id="order_id"]/div/div/div/input')
        self.order_info_select = (By.XPATH, '//*[@id="order_id"]/div/div/dl')
        self.order_confirm = (By.XPATH, '//*[@id="order_id"]/div/div/dl/dd[2]')
        self.daifa_type = (By.XPATH, '//*[@id="modal_form"]/div[2]/div/div[1]/div')
        self.luodi_company_select = (By.XPATH, '//*[@id="modal_form"]/div[4]/div/div/div/div/input')
        self.luodi_company_confirm = (By.XPATH, '//*[@id="modal_form"]/div[4]/div/div/div/dl/dd[3]')
        self.luodi_company_type_select = (By.XPATH, '//*[@id="leibie"]/div/div/div/div/input')
        self.luodi_type = (By.XPATH, '//*[@id="leibie"]/div/div/div/dl/dd[2]')
        self.daifa_count = (By.XPATH, '//*[@id="modal_form"]/div[6]/div[1]/div/input')
        self.daifa_money = (By.XPATH, '//*[@id="modal_form"]/div[6]/div[2]/div/input')
        self.daifa_code = (By.XPATH, '//*[@id="LAY-user-login-vercode"]')
        self.daifa_pwd = (By.XPATH, '//*[@id="modal_form"]/div[9]/div/div/input')
        self.up_load_01 = (By.XPATH, '//*[@id="avatar"]')
        self.up_load_02 = (By.XPATH, '//*[@id="modal_form"]/div[12]/div/input[2]')
        self.submit_btn = (By.XPATH, '//*[@id="modal_form"]/div[13]/div/button[1]')


    def get_iframe1(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe1))
        # return DriverUntil.get_driver().find_element(*self.iframe1)

    def get_d_service(self):
        return WebDriverWait(DriverUntil.get_driver(), 15, poll_frequency=0.5).until(lambda x: x.find_element(*self.d_service))

    def get_d_iframe2(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe2))

    def get_order_info(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_info))

    def get_order_info_select(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_info_select))

    def get_order_confirm(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_confirm))

    def get_daifa_type(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.daifa_type))
        # return DriverUntil.get_driver().find_element(*self.daifa_type)

    def get_luodi_company_select(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.luodi_company_select))
        # return DriverUntil.get_driver().find_element(*self.luodi_company_select)

    def get_luodi_company_confirm(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.luodi_company_confirm))


    def get_luodi_company_type_select(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.luodi_company_type_select))

    def get_luodi_type(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.luodi_type))


    def get_daifa_count(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.daifa_count))
        # return DriverUntil.get_driver().find_element(*self.daifa_count)

    def get_daifa_money(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.daifa_money))
        # return DriverUntil.get_driver().find_element(*self.daifa_money)

    def get_daifa_code(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.daifa_code))
        # return DriverUntil.get_driver().find_element(*self.daifa_code)

    def get_daifa_pwd(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.daifa_pwd))
        # return DriverUntil.get_driver().find_element(*self.daifa_pwd)

    def get_up_load_01(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.up_load_01))
        # return DriverUntil.get_driver().find_element(*self.up_load_01)

    def get_up_load_02(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.up_load_02))
        # return DriverUntil.get_driver().find_element(*self.up_load_02)

    def get_submit_btn(self):
        return WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.submit_btn))
        # return DriverUntil.get_driver().find_element(*self.submit_btn)