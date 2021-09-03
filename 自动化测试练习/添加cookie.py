from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://xdclass.net/")

driver.add_cookie({"name": "head_img", "value":"https%3A//xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/14.jpeg"})
driver.add_cookie({"name": "name", "value":"%u8303%u6842%u82B324"})
driver.add_cookie({"name": "token", "value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTQuanBlZyIsImlkIjo2NzkwNjg3LCJuYW1lIjoi6IyD5qGC6IqzMjQiLCJpYXQiOjE2MjU1NTc3MDYsImV4cCI6MTYyNjE2MjUwNn0.uacTNPO4-wQDniNR9z9krfzlbrxPfoijk3gTYRgyaZ4"})

driver.find_element_by_css_selector("#app > div > div.hot > div > div.content > a:nth-child(1) > div > img").click()

# driver.find_element_by_css_selector("#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a").click()
