import time
import unittest
import HTMLTestRunner
import logging
from selenium.webdriver.support.wait import WebDriverWait
from hy_login.login_business import LoginBusiniss
from hy_login.untils import DriverUntil
from parameterized import parameterized
import json
# from config.time_logging import init_logging_config





def get_data():
    with open("../data/login_data_json.json", encoding="utf-8") as f:
        list = []
        data = json.load(f)
        for dict in data.values():
            list.append((dict.get("username"), dict.get("password"), dict.get("code"), dict.get("login_info")))
        return list


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUntil.get_driver()
        cls.test_proxy = LoginBusiniss()

    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()

    def setUp(self):
        self.driver.get("http://test.gzhyyun.com/")

    @parameterized.expand(get_data())
    def test_login(self, username, password, code, assert_info):
        # logging.info("username={}, password={}, code={}, assert_info={}".format(username, password, code, assert_info))
        logging.info("登录测试")
        self.test_proxy.login(username, password, code)
        login_txt = WebDriverWait(DriverUntil.get_driver(), 15, poll_frequency=0.5).until(lambda x: x.find_element_by_xpath('//div[@class="layui-layer-content layui-layer-padding"]'))
        self.assertIn(assert_info, login_txt.text, msg="断言失败")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTest))
    file = open("../test_report/login_test_report.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(file, title="登录测试报告", description="华翼登录测试用例", verbosity=4)
    runner.run(suite)
