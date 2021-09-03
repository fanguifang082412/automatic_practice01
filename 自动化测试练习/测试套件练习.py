import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        print("set_up")

    def tearDown(self):
        print("teardown")

    def test_001(self):
        print("这是第一个测试用例")

    def test_002(self):
        print("这是第二个测试用例")

    def test_003(self):
        print("这是第三个测试用例")


if __name__ == '__main__':
    unittest.main()
