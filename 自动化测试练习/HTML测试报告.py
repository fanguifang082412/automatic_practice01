import HTMLTestRunner
import unittest
import time


class XdTestUser(unittest.TestCase):
    def setUp(self):
        self.age = 32
        print("set_up")

    def tearDown(self):
        print("tear_down")

    def test_one(self):
        print("用例1")
        self.assertEqual("xd".upper(), "XD")

    def test_two(self):
        print("用例2")
        self.assertTrue("XD".isupper())

    def test_three(self):
        print("用例3")
        self.assertEqual(self.age, 32)


if __name__ == '__main__':
    print("hello")
    suite = unittest.TestSuite()
    suite.addTest(XdTestUser("test_one"))
    suite.addTest(XdTestUser("test_two"))
    suite.addTest(XdTestUser("test_three"))
    # runner = unittest.TextTestRunner(verbosity=0)
    # runner.run(suite)
    # file_str = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    fp = open("./test_report.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
    runner.run(suite)
    fp.close()


