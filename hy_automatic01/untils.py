from selenium import webdriver


class DriverUntil:
    driver = None
    #获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = None
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            # cls.driver.get("http://test.gzhyyun.com/")
        return cls.driver

    #关闭浏览器驱动，并重置为空
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None