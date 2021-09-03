import json
import unittest
import time
from parameterized import parameterized
from selenium.webdriver.support.wait import WebDriverWait
from hy_login.login_business import LoginBusiniss
from hy_login.untils import DriverUntil
from hy_recharge.recharge_business import RechargeBusiness


def recharge_data():

    with open("../data/recharge_data.json", encoding="utf-8") as f:
        list = []
        recharge_test_data = json.load(f)
        for data in recharge_test_data.values():
            list.append((data.get("money"), data.get("image"), data.get("assert_info")))
        return list


class RechargeCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.recharge = RechargeBusiness()
        cls.driver = DriverUntil.get_driver()
        cls.login_business = LoginBusiniss()
        cls.driver.get("http://test.gzhyyun.com/")
        cls.login_business.login("心悦有限公司", "666666", 8888)

    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()

    def setUp(self):
        time.sleep(2)
        DriverUntil.get_driver().get("http://test.gzhyyun.com/")
        self.recharge.switch_iframe1()

    @parameterized.expand(recharge_data())
    def test_recharge(self, money, ur, except_info):
        time.sleep(1)
        self.recharge.company_recharge(money, ur)
        try:
            self.recharge_info = WebDriverWait(DriverUntil.get_driver(), 15, poll_frequency=0.5).until(lambda x: x.find_element_by_xpath('//*[@class="layui-layer-content layui-layer-padding"]'))

            self.assertIn(except_info, self.recharge_info.text, msg="断言失败")

        except Exception as e:
            self.info = DriverUntil.get_driver().find_element_by_css_selector("#LAY_adminError")
            self.assertIn(except_info, self.info.text, msg="断言失败")


if __name__ == "__main__":
    unittest.main()