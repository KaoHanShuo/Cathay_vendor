from driver import Driver
from element import *


class UnitAction(object):
    """常規動作"""

    def __init__(self, driver: Driver):
        self.driver = driver
        self.log = self.driver.logger

    def goto_url(self, url: str):
        """前往網址"""
        self.log.info(self.goto_url.__doc__ + f"- {url}")
        self.driver.driver.get(url)


class UnitHomePage(object):
    """首頁操作"""

    def __init__(self, driver: Driver, element: HomePage):
        self.driver = driver
        self.element = element
        self.log = self.driver.logger

    def screen_shot_home(self, path: str):
        """截圖首頁"""
        self.log.info(self.screen_shot_home.__doc__ + f" - {path}")
        self.driver.screen_shot(path)

    # def get_homepage_open_account(self):
    #     """取得首頁 - 開戶"""
    #     self.element.homepage_open_account
    #     self.log.info(self.get_homepage_open_account.__doc__)

    def click_hamburger_menu(self):
        """點擊左上功能列"""
        self.log.info(self.click_hamburger_menu.__doc__)
        self.driver.element_click(self.element.hamburger_menu)


class UnitSideMenuList(object):
    """側邊選單清單"""

    def __init__(self, driver: Driver, element: SideMenuList):
        self.driver = driver
        self.element = element
        self.log = self.driver.logger

    def click_prod_introduce(self):
        """點擊產品介紹"""
        self.log.info(self.click_prod_introduce.__doc__)
        self.driver.element_click(self.element.prod_introduce)

    def click_prod_introduce_card(self):
        """點擊產品介紹 - 信用卡"""
        self.log.info(self.click_prod_introduce_card.__doc__)
        self.driver.element_click(self.element.prod_introduce_card)

    def click_prod_introduce_card_card_intro(self):
        """點擊產品介紹 - 信用卡 - 卡片介紹"""
        self.log.info(self.click_prod_introduce_card_card_intro.__doc__)
        self.driver.element_click(self.element.prod_introduce_card_card_intro)

    def screen_shot_prod_introduce_card_list(self, path: str):
        """截圖產品介紹 - 信用卡清單"""
        print(self.element.prod_introduce_card_list)
        self.log.info(self.screen_shot_prod_introduce_card_list.__doc__ + f" - {path}")
        self.element.prod_introduce_card_list.screenshot(path)

    def get_num_prod_introduce_card_list(self):
        """計數產品介紹 - 信用卡清單"""
        self.log.info(self.get_num_prod_introduce_card_list.__doc__)
        return len(list(self.element.prod_introduce_card_list_Child))

class UnitCardIntroducePage(object):
    """卡片介紹頁面"""
    def __init__(self, driver: Driver, element: CardIntroducePage):
        self.driver = driver
        self.element = element
        self.log = self.driver.logger

    def scroll_to_pagination(self):
        """滾動到分頁物件"""
        self.log.info(self.scroll_to_pagination.__doc__)
        self.driver.scroll_to_element(self.element.swiper_pagination)

    def count_pagination_bullets(self):
        """計數分頁子項目"""
        self.log.info(self.count_pagination_bullets.__doc__)
        return len(self.element.pagination_bullets)
    def click_pagination_bullets(self, num:int):
        """點擊分頁子項目"""
        self.log.info(self.click_pagination_bullets.__doc__)
        self.driver.element_click(self.element.pagination_bullets[num])
class Unit(object):

    def __init__(self, driver: Driver, element: Element):
        self.driver = driver
        self.__unit_action = UnitAction(driver)
        self.__unit_homePage = UnitHomePage(driver, element.home_page)
        self.__unit_sideMenuList = UnitSideMenuList(driver, element.side_menu_list)
        self.__unit_cardIntroducePage = UnitCardIntroducePage(driver, element.card_introduce_page)
    @property
    def unit_action(self):
        return self.__unit_action

    @property
    def unit_homePage(self):
        return self.__unit_homePage

    @property
    def unit_sideMenuList(self):
        return self.__unit_sideMenuList
    
    @property
    def unit_cardIntroducePage(self):
        return self.__unit_cardIntroducePage

