from selenium.webdriver.common.by import By
from hy_login import untils
from hy_login.untils import DriverUntil


class InvoicePage:

    def __init__(self):
        self.invoice_info = (By.XPATH, '//*[@id="LAY-system-side-menu"]/li/dl[5]/dd/dl/dd[1]/a')
        self.iframe1 = (By.CSS_SELECTOR, '#LAY_app_body > div.layadmin-tabsbody-item.layui-show > iframe')
        self.apply_invoice = (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[8]/div/a[1]')
        self.iframe2 = (By.XPATH, '//iframe[@src="/company/invoice/apply_invoice.html?company_id=10000000000263&french_company_id=10000000000177&invoicetype=1001"]')
        self.invoice_money = (By.XPATH, '/html/body/div/div/div/div/form/div[1]/div/div/input')
        self.invoice_type_select = (By.XPATH, '/html/body/div/div/div/div/form/div[2]/div/div/div/div/input')
        self.invoice_type_comfirm = (By.XPATH, '/html/body/div/div/div/div/form/div[2]/div/div/div/dl/dd[2]')
        self.invoice_project_select = (By.XPATH, '/html/body/div/div/div/div/form/div[3]/div/div/div/div/input')
        self.invoice_project_confirm = (By.XPATH, '/html/body/div/div/div/div/form/div[3]/div/div/div/dl/dd[3]')
        self.invoice_beizhu = (By.XPATH, '/html/body/div/div/div/div/form/div[4]/div/div/textarea')
        self.invoice_submit_btn = (By.XPATH, '/html/body/div/div/div/div/form/div[6]/div/button[1]')

    def get_invoice_info(self):
        return untils.get_element(self.invoice_info)

    def get_iframe1(self):
        return untils.get_element(self.iframe1)

    def get_apply_invoice(self):
        return untils.get_element(self.apply_invoice)

    def get_iframe2(self):
        return untils.get_element(self.iframe2)

    def get_invoice_money(self):
        return untils.get_element(self.invoice_money)

    def get_invoice_type_select(self):
        return untils.get_element(self.invoice_type_select)

    def get_invoice_type_comfirm(self):
        return untils.get_element(self.invoice_type_comfirm)

    def get_invoice_project_select(self):
        return untils.get_element(self.invoice_project_select)

    def get_invoice_project_confirm(self):
        return untils.get_element(self.invoice_project_confirm)

    def get_invoice_invoice_beizhu(self):
        return untils.get_element(self.invoice_beizhu)

    def get_invoice_submit_btn(self):
        return untils.get_element(self.invoice_submit_btn)


