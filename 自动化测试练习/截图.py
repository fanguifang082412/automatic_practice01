from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://xdclass.net/")
ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)")
ActionChains(driver).move_to_element(ele).perform()
try:
    driver.find_element_by_id("kw")
except:
    driver.get_screenshot_as_file("./error.png")
