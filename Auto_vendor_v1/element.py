from driver import Driver


class HomePage(object):
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def hamburger_menu(self):
        """左上功能列"""
        return self.driver.get_ele_by_xpath("//div[@class='cubre-o-header__burger']")


class SideMenuList(object):
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def prod_introduce(self):
        """產品介紹"""
        return self.driver.get_elements_by_xpath(
            None, "//div[@class='cubre-o-menu']//div[@class='cubre-a-menuSortBtn -l1']"
        )[0]

    @property
    def prod_introduce_card(self):
        """信用卡"""
        return self.driver.get_ele_by_xpath(
            "//div[@class='cubre-o-menu__content']//div[@class='cubre-a-menuSortBtn' and contains(text(), '信用卡')]"
        )

    @property
    def prod_introduce_card_list(self):
        """信用卡 - 清單"""
        return self.driver.get_ele_by_xpath(
            "//div[@class='cubre-a-menuSortBtn cubre-u-mbOnly' and contains(text(), '信用卡')]/parent::div"
        )

    @property
    def prod_introduce_card_list_Child(self):
        """信用卡 - 清單下的子元素"""
        return self.driver.get_elements_by_xpath(self.prod_introduce_card_list, ".//a")

    @property
    def prod_introduce_card_card_intro(self):
        """信用卡 - 卡片介紹"""
        return self.driver.get_elements_by_xpath(self.prod_introduce_card_list, ".//a")[
            0
        ]


class CardIntroducePage(object):
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def swiper_pagination(self):
        """滑動分頁的物件"""
        return self.driver.get_elements_by_xpath(
            None,
            "//div[@class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']",
        )[4]

    @property
    def pagination_bullets(self):
        """分頁的子項目"""
        return self.driver.get_elements_by_xpath(self.swiper_pagination, ".//span")


class Element(object):
    def __init__(self, driver: Driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.side_menu_list = SideMenuList(driver)
        self.card_introduce_page = CardIntroducePage(driver)
