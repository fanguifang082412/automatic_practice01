from hy_automatic01.untils import DriverUntil


class PageBase:

    def find_element(self, location):
       return DriverUntil.get_driver().find_element(*location)




class ActionBase:

    def input_text(self, element, text):
        element.send_keys(text)