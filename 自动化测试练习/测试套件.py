import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.age = 32
        print("set_up")

    def tearDown(self) :
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


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestUser("test_one"))
    suite.addTest(TestUser("test_two"))
    suite.addTest(TestUser("test_three"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

