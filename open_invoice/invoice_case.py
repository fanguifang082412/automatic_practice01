import unittest
from selenium.webdriver.common.by import By
from hy_login.login_business import LoginBusiniss
from open_invoice.invoice_business import InvoiceBusiness
from hy_login.untils import DriverUntil
from hy_login import untils


class InvoiceDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.invoice_business = InvoiceBusiness()
        cls.login_business = LoginBusiniss()
        cls.driver = DriverUntil.get_driver()

    @classmethod
    def tearDownClass(cls):
        DriverUntil.quit_driver()

    def setUp(self):
        self.driver.get("http://test.gzhyyun.com/")

    def test_apply_invoice(self):
        self.login_business.login("心悦有限公司", "666666", 8888)
        self.invoice_business.invoice_business("0.01", "测试")
        invoice_tishi = (By.XPATH, '//*[@class="layui-layer-content layui-layer-padding"]')
        invoice_in = untils.get_element(invoice_tishi)
        invoice_success_info = invoice_in.text
        self.assertIn("申请成功", invoice_success_info)


if __name__ == "__main__":
    unittest.main()