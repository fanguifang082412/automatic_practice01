import time
import unittest
from hy_daifa.daifa_business import DaifaBusiness
from hy_login.login_business import LoginBusiniss
from hy_login.untils import DriverUntil
from selenium.webdriver.support.wait import WebDriverWait

class DaifaDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUntil.get_driver()
        cls.daifa_demo = DaifaBusiness()
        cls.login_business = LoginBusiniss()

    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()

    def setUp(self):
        self.driver.get("http://test.gzhyyun.com/")
        self.login_business.login("心悦有限公司", "666666", 8888)

    def test_daifa(self):
        self.daifa_demo.daifa_business(1, 100, "6666", "123456", r"C:\Users\Administrator\Desktop\daifujilu.xlsx", r"C:\Users\Administrator\Desktop\001.zip")
        try:
            daifa_success_tip = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element_by_xpath('//*[@id="layui-layer3"]/div'))
            self.assertIn("提交成功", daifa_success_tip.text)

        except Exception as E:
            daifa_fail_tip = DriverUntil.get_driver().find_element_by_css_selector('#LAY_adminError')
            print(daifa_fail_tip.text)


if __name__ == "__main__":
    unittest.main()
