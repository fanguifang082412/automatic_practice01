import time
import unittest
from hy_automatic01.login_business import LoginBusiniss
from parameterized import parameterized
from hy_automatic01.untils import DriverUntil
import json


def login_data():
    data_list = []
    with open("../data/login_data_json.json", encoding="utf-8") as f:
        test_data = json.load(f)
        for data in test_data.values():
            data_list.append((data.get("username"),data.get("password"),data.get("code"),data.get("login_info")))

    return data_list


class LoginTest(unittest.TestCase):
#
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUntil.get_driver()
        cls.login_business = LoginBusiniss()
#
    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()
#
    def setUp(self):
        self.driver.get("http://test.gzhyyun.com/")

    @parameterized.expand(login_data())
    def test_login01(self, username, pwd, code, assert_info):
        self.login_business.login_demo(username, pwd, code)
        time.sleep(1)
        login_info = DriverUntil.get_driver().find_element_by_css_selector('.layui-layer-content').text
        self.assertIn(assert_info, login_info)


if __name__ == "__main__":
    unittest.main()