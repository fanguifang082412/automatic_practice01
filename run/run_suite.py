import unittest
from hy_daifa.daifa_demo import DaifaDemo
from hy_login.login_demo import LoginTest
from hy_order.order_demo import AddOrderDemo
from hy_order_check.check_demo import CheckOrderDemo
import HTMLTestRunner
from hy_recharge.recharge_demo import RechargeCase
from open_invoice.invoice_case import InvoiceDemo


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(AddOrderDemo))

suite.addTest(unittest.makeSuite(CheckOrderDemo))

suite.addTest(unittest.makeSuite(LoginTest))

suite.addTest(unittest.makeSuite(DaifaDemo))

suite.addTest(unittest.makeSuite(RechargeCase))

suite.addTest(unittest.makeSuite(InvoiceDemo))



file = open("../test_report/add_order_report.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(file, title="测试报告", description="关于华翼税通平台主要功能的自动化测试", verbosity=4)

runner.run(suite)
