from hy_login.untils import DriverUntil
from open_invoice.voice_page import InvoicePage


class InvoiceAction:
    def __init__(self):
        self.invoice_page = InvoicePage()

    def click_invoice_info(self):
        self.invoice_page.get_invoice_info().click()

    def switch_iframe1(self):
        DriverUntil.get_driver().switch_to.frame(self.invoice_page.get_iframe1())

    def click_apply_invoice(self):
        self.invoice_page.get_apply_invoice().click()

    def switch_iframe2(self):
        DriverUntil.get_driver().switch_to.frame(self.invoice_page.get_iframe2())

    def input_invoice_money(self, money):
        self.invoice_page.get_invoice_money().send_keys(money)

    def click_invoice_type_select(self):
        self.invoice_page.get_invoice_type_select().click()

    def click_invoice_type_comfirm(self):
        self.invoice_page.get_invoice_type_comfirm().click()

    def click_invoice_project_select(self):
        self.invoice_page.get_invoice_project_select().click()

    def click_invoice_project_confirm(self):
        self.invoice_page.get_invoice_project_confirm().click()

    def input_invoice_invoice_beizhu(self, info):
        self.invoice_page.get_invoice_invoice_beizhu().send_keys(info)

    def click_invoice_submit_btn(self):
        self.invoice_page.get_invoice_submit_btn().click()
