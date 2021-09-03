import  time
import unittest
import HTMLTestRunner
# file_str = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
# print(file_str)
#
# file_str = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
# file_result = open("./"+file_str+"_result.html", "wb")
# print(file_str)
# file_result.close()
#
# fp = open("./test_report.html", "wb")
# fp.close()


class XdTestUser(unittest.TestCase):
    def setUp(self):
        self.age = 32
        print("set_up")

    def tearDown(self):
        print("tear_down")

    def test_one(self):
        u"这是用例1"
        print("用例1")
        self.assertEqual("xd".upper(), "XD")

    def test_two(self):
        u"这是用例2"
        print("用例2")
        self.assertTrue("XD".isupper())

    def test_three(self):
        u"这是用例3"
        print("用例3")
        self.assertEqual(self.age, 32)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(XdTestUser("test_two"))
    suite.addTest(XdTestUser("test_one"))
    suite.addTest(XdTestUser("test_three"))
    file_ele = time.strftime("%Y-%m-%d %H-%M-%S")
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    fp = open("C:/Users/Administrator/PycharmProjects/pythonProject"+file_ele+".html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="测试报告练习")
    runner.run(suite)
    fp.close()