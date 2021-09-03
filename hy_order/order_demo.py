import unittest
from hy_login.login_business import LoginBusiniss
from hy_login.untils import DriverUntil
from hy_order.order_business import OrderBusiness
from selenium.webdriver.support.wait import WebDriverWait


class AddOrderDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUntil.get_driver()
        cls.login_business = LoginBusiniss()
        cls.order_business = OrderBusiness()


    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()

    def setUp(self):
        self.driver.get("http://test.gzhyyun.com/")
        self.login_business.login("心悦有限公司", "666666", 8888)

    def test_add_order(self):
        self.order_business.add_order("测试项目", "hy测试项目", "订单类型", "项目内容", "项目条件", "10", "100")
        add_order_btn = WebDriverWait(DriverUntil.get_driver(), 10, poll_frequency=0.5).until(lambda x: x.find_element_by_css_selector("#layui-layer3 > div"))
        self.assertIn("添加成功", add_order_btn.text)


if __name__ == "__main__":
    unittest.main()