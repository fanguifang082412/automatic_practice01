from open_invoice.invoice_action import InvoiceAction


class InvoiceBusiness:

    def __init__(self):
        self.invoice_action = InvoiceAction()

    def invoice_business(self, money, info):
        self.invoice_action.click_invoice_info()
        self.invoice_action.switch_iframe1()
        self.invoice_action.click_apply_invoice()
        self.invoice_action.switch_iframe2()
        self.invoice_action.input_invoice_money(money)
        self.invoice_action.click_invoice_type_select()
        self.invoice_action.click_invoice_type_comfirm()
        self.invoice_action.click_invoice_project_select()
        self.invoice_action.click_invoice_project_confirm()
        self.invoice_action.input_invoice_invoice_beizhu(info)
        self.invoice_action.click_invoice_submit_btn()
