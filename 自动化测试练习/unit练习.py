import unittest

class UserTestCase(unittest.TestCase):
    def setUp(self):
        print("打开浏览器")

    def tearDown(self):
        print("退出浏览器")

    def test_001(self):
        print("登录")

if __name__ == "__main__":
    unittest.main()




