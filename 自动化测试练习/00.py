from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://xdclass.net")


login_ele = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)")
login_ele.click()
phone_input = driver.find_element_by_xpath("//div[@class='mobienum']/input")
phone_input.clear()
phone_input.send_keys("19958722846")
pwd_input = driver.find_element_by_xpath("//input[@type='password']")
pwd_input.clear()
pwd_input.send_keys("fang082412")
login_btn = driver.find_element_by_xpath("//button[@class='btn']")
login_btn.click()
driver.implicitly_wait(5)
user_image = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.r_userinfo.f_r > div.avatar.f_r > img")
# driver.implicitly_wait(5)
ActionChains(driver).move_to_element(user_image).perform()
user_info = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.nav_container > div > div > div.time > p:nth-child(1)")
print(user_info.text)

# user_name = driver.find_element_by_css_selector("#app > div > div:nth-child(1) > div.header > div.nav_container > div > div > div.user > p")



