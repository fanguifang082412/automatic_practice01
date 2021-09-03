from hy_login.untils import DriverUntil
from config.time_logging import init_logging_config

init_logging_config()


class PageBase:

    def find_element(self, location):
       return DriverUntil.get_driver().find_element(*location)



class ActionBase:

    def input_text(self, element, text):
        element.send_keys(text)