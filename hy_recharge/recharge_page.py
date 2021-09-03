from selenium.webdriver.common.by import By
from hy_login.untils import DriverUntil
from hy_login.base import PageBase


class RechageDemo(PageBase):
    def __init__(self):
        # self.company_home = (By.CSS_SELECTOR, "dd.layui-this > a:nth-child(1)")
        self.recharge = (By.CSS_SELECTOR, "h3.recharge:nth-child(1)")
        self.recharge_company_select = (By.XPATH, '//*[@id="modal_form"]/div[2]/div/div/div/input')
        self.recharge_company = (By.XPATH, '//*[@id="modal_form"]/div[2]/div/div/dl/dd[2]')
        self.recharge_money = (By.CSS_SELECTOR, "div.layui-col-lg3:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        self.image_upload = (By.XPATH, "/html/body/div/div/form/div[6]/div[2]/div/input")
        self.recharge_submit = (By.CSS_SELECTOR, "div.layui-input-block:nth-child(1) > button:nth-child(1)")
        self.iframe1 = (By.XPATH, "//div[@class='layadmin-tabsbody-item layui-show']/iframe")
        self.iframe2 = (By.XPATH, '//iframe[@allowtransparency="true" and @id="layui-layer-iframe1"]')


    # def get_company_home(self):
    #     return DriverUntil.get_driver().find_element(*self.company_home)


    def get_recharge(self):
        return DriverUntil.get_driver().find_element(*self.recharge)

    def get_recharge_company_select(self):
        return DriverUntil.get_driver().find_element(*self.recharge_company_select)

    def get_recharge_company(self):
        return DriverUntil.get_driver().find_element(*self.recharge_company)

    def get_recharge_money(self):
        return DriverUntil.get_driver().find_element(*self.recharge_money)

    def find_image_upload(self):
        return DriverUntil.get_driver().find_element(*self.image_upload)

    def get_recharge_submit(self):
        return DriverUntil.get_driver().find_element(*self.recharge_submit)

    def get_iframe1(self):
        return DriverUntil.get_driver().find_element(*self.iframe1)

    def get_iframe2(self):
        return DriverUntil.get_driver().find_element(*self.iframe2)




