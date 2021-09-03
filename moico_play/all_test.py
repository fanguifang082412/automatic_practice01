import unittest
import HTMLTestRunner
import time
import login_order,  menu_perform
from mail_demo import MailUtils

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login_order.LoginTest))
    suite.addTest(unittest.makeSuite(menu_perform.MenuForm))
    return suite


if __name__ == "__main__":
    suite = create_suite()
    # file_str = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    file = open("../test_report/report" + ".html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="综合测试报告", description="多模块测试用例", verbosity=2)
    runner.run(suite)
    file.close()
    MailUtils.send_report()




