from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://xdclass.net")
ele1 = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)")
ActionChains(driver).move_to_element(ele1).perform()
driver.implicitly_wait(3)
ele2 = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(1)")
ele2.click()