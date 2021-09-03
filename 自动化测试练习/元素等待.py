from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
# driver.implicitly_wait(5)
try:
    ele = WebDriverWait(driver, 5, poll_frequency=0.5).until(ec.presence_of_element_located((By.ID, "kw")))
    ele.send_keys("小D课堂")
    sleep(3)
    print("资源加载成功")
except:
    print("资源加载失败")
finally:
    driver.quit()

