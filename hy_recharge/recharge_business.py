from hy_recharge.recharge_action import RechageAction
import time


class RechargeBusiness:

    def __init__(self):
        self.recharge_action = RechageAction()


    def switch_iframe1(self):
    # 切换iframe1
        time.sleep(3)
        self.recharge_action.switch_iframe1()
    # 点击充值按钮
        self.recharge_action.click_recharge()


    def company_recharge(self, money, ur):

        # iframe = DriverUntil.get_driver().find_element_by_xpath("//div[@class='layadmin-tabsbody-item layui-show']/iframe")
        # DriverUntil.get_driver().switch_to.frame(iframe)

        # 切换iframe2
        self.recharge_action.switch_iframe2()
        # fr = DriverUntil.get_driver().find_element_by_xpath('//iframe[@allowtransparency="true" and @id="layui-layer-iframe1"]')
        # DriverUntil.get_driver().switch_to.frame(fr)

        #进行充值操作
        time.sleep(3)
        self.recharge_action.click_recharge_company_select()
        self.recharge_action.click_recharge_company()

        time.sleep(3)
        self.recharge_action.input_money(money)
        self.recharge_action.click_image_upload(ur)
        time.sleep(2)
        self.recharge_action.submit_btn()






