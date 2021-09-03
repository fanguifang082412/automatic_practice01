import unittest


class UserTest(unittest.TestCase):

    def setUp(self):
        print("set_up")

    def tearDown(self):
        print("tear_down")

    def test_001(self):
        print("第一个用例")


# if __name__ == "__main__":
#     unittest.main()

user = UserTest()
user.test_001()