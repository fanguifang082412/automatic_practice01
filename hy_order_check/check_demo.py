from hy_login.login_business import LoginBusiniss
from hy_order_check.check_business import CheckBusiness
import unittest
from hy_login.untils import DriverUntil
from selenium.webdriver.support.wait import WebDriverWait


class CheckOrderDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.check_business = CheckBusiness()
        cls.login_b = LoginBusiniss()


    # @classmethod
    # def tearDownClass(cls):
    #     DriverUntil.quit_driver()

    def setUp(self):
        self.driver = DriverUntil.get_driver()
        self.driver.get("http://test.gzhyyun.com/")

    def tearDown(self):
        DriverUntil.quit_driver()


    def test_check_order_01(self):
        self.login_b.login("yunying01", "666666", "8888")
        self.check_business.order_check_01("测试yunying01审核订单", "666666", "123456")
        assert_ele_01 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element_by_css_selector("#layui-layer2 > div"))
        assert_info_01 = assert_ele_01.text
        self.assertIn("审核成功", assert_info_01)


    def test_check_order_02(self):
        self.login_b.login("yunying02", "666666", "8888")
        self.check_business.order_check_02("测试yunying02审核订单", "666666", "123456")
        assert_ele_02 = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element_by_css_selector("#layui-layer2 > div"))
        assert_info_02 = assert_ele_02.text
        self.assertIn("审核成功", assert_info_02)



if __name__ == "__main__":
    unittest.main()