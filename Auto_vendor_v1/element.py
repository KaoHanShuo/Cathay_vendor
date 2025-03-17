from driver import Driver


class HomePage(object):
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def hamburger_menu(self):
        """左上功能列"""
        return self.driver.get_ele_by_xpath("//div[@class='cubre-o-header__burger']")

    @property
    def prod_introduce(self):
        """產品介紹"""
        return self.driver.get_ele_by_xpath(self.prod_introduce)

    @property
    def prod_introduce_card(self):
        """信用卡"""
        return self.driver.get_ele_by_xpath(self.prod_introduce_card)

    @property
    def prod_introduce_card_list(self):
        """信用卡 - 清單"""
        return self.driver.get_ele_by_xpath(self.prod_introduce_card_list)

    @property
    def prod_introduce_card_list_Child(self):
        """信用卡 - 清單下的子元素"""
        return self.driver.get_ele_by_xpath(self.prod_introduce_card_list_Child)

    @property
    def card_type(self):
        """信用卡 - 信用卡介紹 - 信用卡類型清單"""
        return self.driver.get_ele_by_xpath(self.card_type)

    @property
    def card_type_Child(self):
        """信用卡 - 信用卡介紹 - 信用卡類型清單的子元素"""
        return self.driver.get_ele_by_xpath(self.card_type_Child)


class Element(object):
    def __init__(self, driver: Driver):
        self.driver = driver
        self.homePage = HomePage(driver)
