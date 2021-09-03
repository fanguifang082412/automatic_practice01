from selenium.webdriver.common.by import By
from hy_login.untils import DriverUntil
from selenium.webdriver.support.wait import WebDriverWait


class CheckOrderPage:

    def __init__(self):
        # 运营一审页面元素
        self.order_list = (By.XPATH, '//*[@id="LAY-system-side-menu"]/li/dl[1]/dd/dl/dd[9]/a')
        self.iframe1 = (By.XPATH, '//*[@id="LAY_app_body"]/div[2]/iframe')
        self.order_status = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div')
        self.order_check1 = (By.PARTIAL_LINK_TEXT, '订单一审')
        self.iframe2 = (By.XPATH, '//*[@id="layui-layer-iframe1"]')
        self.check_info = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[1]/div/textarea')
        self.check_code = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[2]/div/div/input')
        self.check_pwd = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[3]/div/input')
        self.check_pass_select = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[4]/div/div[1]/div')
        self.check_submit_btn = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[5]/div/div/button[1]')
        self.yunying_account = (By.XPATH, '//*[@id="LAY_app"]/div/div[1]/ul[2]/li[2]/a/cite')
        self.exit = (By.XPATH, '//*[@id="LAY_app"]/div/div[1]/ul[2]/li[2]/dl/dd[4]')
        self.exit_account = (By.XPATH, '//*[@id="LAY_app"]/div/div[1]/ul[2]/li[2]/dl/dd[4]/a')

        #运营二审页面元素

        self.order_list2 = (By.XPATH, '//*[@id="LAY-system-side-menu"]/li/dl[1]/dd/dl/dd[8]/a')
        self.iframe1_2 = (By.XPATH, '//*[@id="LAY_app_body"]/div[2]/iframe')
        self.order_status_2 = (By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[8]/div/a[1]')
        self.order_check2 = (By.PARTIAL_LINK_TEXT, '订单二审')
        self.iframe2_2 = (By.XPATH, '//*[@id="layui-layer-iframe1"]')
        self.check_info_2 = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[1]/div/textarea')
        self.check_code_2 = (By.XPATH, '//*[@id="LAY-user-login-vercode"]')
        self.check_pwd_2 = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[4]/div/input')
        self.check_pass_select_2 = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[5]/div/div[1]/i')
        self.check_submit_btn_2 = (By.XPATH, '//*[@id="layuiadmin-form-admin"]/form/div[6]/div/div/button[1]')
        self.yunying_account_2 = (By.XPATH, '//*[@id="LAY_app"]/div/div[1]/ul[2]/li[2]/a/cite')
        self.exit_2 = (By.XPATH, '//*[@id="LAY_app"]/div/div[1]/ul[2]/li[2]/dl/dd[5]')


    #定位运营一账号的页面元素

    def get_order_list(self):
        get_order_list_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_list))
        return get_order_list_ele

    def get_iframe1(self):
        iframe1_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe1))
        return iframe1_ele

    def get_order_status(self):
        order_status_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_status))
        return order_status_ele

    def get_order_check1(self):
        order_check1_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_check1))
        return order_check1_ele

    def get_iframe2(self):
        iframe2_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe2))
        return iframe2_ele

    def get_check_info(self):
        get_check_info_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_info))
        return get_check_info_ele

    def get_check_code(self):
        get_check_code_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_code))
        return get_check_code_ele

    def get_check_pwd(self):
        get_check_pwd_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_pwd))
        return get_check_pwd_ele

    def get_check_pass_select(self):
        get_check_pass_select_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_pass_select))
        return get_check_pass_select_ele

    def get_check_submit_btn(self):
        get_check_submit_btn_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_submit_btn))
        return get_check_submit_btn_ele

    def get_yunying_account(self):
        get_yunying_account_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.yunying_account))
        return get_yunying_account_ele

    def get_exit(self):
        get_exit_ele = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.exit))
        return get_exit_ele

    def get_exit_account(self):
        get_exit_account_ele = WebDriverWait(DriverUntil.get_driver(), 20, poll_frequency=0.5).until(lambda x: x.find_element(*self.exit_account))
        return get_exit_account_ele

    # 定位运营二账号的页面元素

    def get_order_list2(self):
        order_list_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_list2))
        return order_list_ele_2

    def get_iframe1_2(self):
        iframe1_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe1_2))
        return iframe1_ele_2

    def get_order_status_2(self):
        order_status_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_status_2))
        return order_status_ele_2

    def get_order_check2(self):
        order_check_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.order_check2))
        return order_check_ele_2

    def get_iframe2_2(self):
        iframe2_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.iframe2_2))
        return iframe2_ele_2

    def get_check_info_2(self):
        check_info_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_info_2))
        return check_info_ele_2

    def get_check_code_2(self):
        check_code_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_code_2))
        return check_code_ele_2

    def get_check_pwd_2(self):
        check_pwd_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_pwd_2))
        return check_pwd_ele_2

    def get_check_pass_select_2(self):
        check_pass_select_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_pass_select_2))
        return check_pass_select_ele_2

    def get_check_submit_btn_2(self):
        check_submit_btn_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.check_submit_btn_2))
        return check_submit_btn_ele_2

    def get_yunying_account_2(self):
        yunying_account_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.yunying_account_2))
        return yunying_account_ele_2

    def get_exit_2(self):
        exit_ele_2 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element(*self.exit_2))
        return exit_ele_2




