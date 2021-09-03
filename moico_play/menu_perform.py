import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MenuForm(unittest.TestCase):
    u"菜单悬浮"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://xdclass.net")

    def tearDown(self):
        self.driver.close()

    def test_menu(self):
        driver = self.driver
        menu_ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(2)")
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(menu_ele).perform()
        p_ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(8)")
        p_ele.click()
        sleep(3)


if __name__ == "__main__":
    unittest.main()