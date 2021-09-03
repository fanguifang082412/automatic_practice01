import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        # self.driver.quit()

    def test_login(self):
        u"测试登录"
        self.driver.get("https://xdclass.net")
        driver = self.driver
        login_ele = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)")
        login_ele.click()
        phone_input = driver.find_element_by_xpath("//div[@class='mobienum']/input")
        phone_input.clear()
        phone_input.send_keys("19958722846")
        pwd_input = driver.find_element_by_xpath("//input[@type='password']")
        pwd_input.click()
        pwd_input.send_keys("fang082412")
        login_btn = driver.find_element_by_xpath("//button[@class='btn']")
        login_btn.click()
        driver.implicitly_wait(3)

        user_image = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.r_userinfo.f_r > div.avatar.f_r > img")
        driver.implicitly_wait(5)
        # ActionChains(driver).move_to_element(user_image).perform()
        # user_info = driver.find_element_by_class_name("username")
        # print(user_info.text)
        # sleep(6)
        ce_ele = driver.find_element_by_partial_link_text("我的学习")
        self.assertIn("我的学习", ce_ele.text, msg="登陆失败")

        # 测试下单
    def test_order(self):
        u"测试下单"
        driver = self.driver
        driver.get("http://old.xdclass.net")
        # 添加cookie
        driver.add_cookie({"name":"head_img","value":"https%3A//xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/14.jpeg"})
        driver.add_cookie({"name":"name","value":"%u8303%u6842%u82B324"})
        driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTQuanBlZyIsImlkIjo2NzkwNjg3LCJuYW1lIjoi6IyD5qGC6IqzMjQiLCJpYXQiOjE2MjYwNTk2NTEsImV4cCI6MTYyNjY2NDQ1MX0.rzDph88iiiJUsF3bdjtcz6qSer2UIMHIt9ut2DTKsxY"})
        # 获取元素
        class_ele = driver.find_element_by_css_selector("#banner_left_ul > a:nth-child(1) > li > span:nth-child(1)")
        ActionChains(driver).move_to_element(class_ele).perform()
        python_ele = driver.find_element_by_css_selector("#active > div.des_top > div.des_one > div.des_text > a:nth-child(1)")
        python_ele.click()
        # 获取所有的句柄
        handles = driver.window_handles
        # 切换到最后一个窗口
        driver.switch_to_window(handles[-1])
        driver.switch_to.window(handles[-1])
        docker_ele = driver.find_element_by_css_selector("#app > div > div.sort_main > div.video > div > div:nth-child(1) > a > div.img1 > img")
        docker_ele.click()
        driver.implicitly_wait(5)
        buy_btn = driver.find_element_by_css_selector("#app > div > div.main > div.main_content.fix > div.main_content_right > div.start_to_learn > div.learn_btn > a")
        buy_btn.click()

        con_order = driver.find_element_by_css_selector("#submitOrder")
        con_order.click()
        sleep(3)
        pay_now = driver.find_element_by_css_selector("#payImmediately")
        pay_now.click()
        sleep(3)
        order_txt = driver.find_element_by_css_selector("#payment > div.all > div > p.code_title")
        weixin_txt = order_txt.text
        sleep(3)
        self.assertIn("微信扫描支付", weixin_txt, msg="下单失败")


# suite = unittest.TestSuite()
# suite.addTest(LoginTest("test_login"))
# suite.addTest(LoginTest("test_order"))
# file = open("./test_report.html", "wb")
# runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="测试报告", description="测试登录下单", verbosity=3)
# runner.run(suite)
# file.close()

if __name__ == "__main__":
    unittest.main()
