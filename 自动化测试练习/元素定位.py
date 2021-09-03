from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://xdclass.net")
sleep(3)
# driver.find_element_by_id("kw").send_keys("小D课堂")
# driver.find_element_by_id("su").click()
# driver.find_element_by_class_name("s_ipt").send_keys("小D课堂")
# driver.find_element_by_id("su").click()
# driver.find_element_by_name("wd").send_keys("小D课堂")
# driver.find_element_by_link_text("超级会员").click()

# 通过css查找元素的方法
# 1. 右键审查元素 > 选择后，右键复制CSS元素路径。简单快捷
# driver.find_element_by_css_selector("#app > div > div.hot > div > div.content > a:nth-child(1) > div > img").click()
# 通过XPath查找元素的方法
# 1. 右键审查元素 > 选择后，右键复制XPath元素路径。简单快捷
driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.m_navitems.f_l > ul > li:nth-child(2)").click()
