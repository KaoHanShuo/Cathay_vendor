from driver import Driver
from element import Element
from unit import Unit
from parameter import *


class Case1:
    """開啟網頁 > 截圖"""

    def __init__(self, unit: Unit):
        self.unit = unit

    def exec_case(self):
        self.unit.unit_homePage.screen_shot_home(pic_folder + "/case1.png")


class Case2(object):
    """點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖"""

    def __init__(self, unit: Unit):

        self.unit = unit
        self.log = self.unit.driver.logger

    def exec_case(self):
        self.unit.unit_homePage.click_hamburger_menu()
        self.unit.unit_sideMenuList.click_prod_introduce()
        self.unit.unit_sideMenuList.click_prod_introduce_card()
        self.unit.unit_sideMenuList.screen_shot_prod_introduce_card_list(
            pic_folder + "/case2.png"
        )
        card_num = self.unit.unit_sideMenuList.get_num_prod_introduce_card_list()
        self.log.info(f"信用卡的數量為 {card_num}")


class Case3(object):
    """個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖"""

    def __init__(self, unit: Unit):
        self.unit = unit
        self.log = self.unit.driver.logger

    def exec_case(self):
        self.unit.unit_homePage.click_hamburger_menu()
        self.unit.unit_sideMenuList.click_prod_introduce()
        self.unit.unit_sideMenuList.click_prod_introduce_card()
        self.unit.unit_sideMenuList.click_prod_introduce_card_card_intro()
        self.unit.unit_cardIntroducePage.scroll_to_pagination()
        for card in range(
            0, self.unit.unit_cardIntroducePage.count_pagination_bullets()
        ):
            self.unit.unit_cardIntroducePage.click_pagination_bullets(card)
            self.unit.unit_homePage.screen_shot_home(
                pic_folder + f"/case3 - {card+1}.png"
            )
        self.log.info(f"所有(停發)信用卡數量為 {card+1}")


class AutoTest(object):
    def __init__(self, device=None, browser=None):
        self.driver = Driver(device, browser)
        self.log = self.driver.logger

    def exec_chrome_case1(self):
        """執行cas1.
        進入home page, 執行case1, 重新loading home page
        """
        try:
            self.driver.get_url(url)
            Case1(Unit(self.driver, Element(self.driver))).exec_case()
            self.log.info("Case1 結束")
        except:
            self.log.warning("Case1 有異常問題")

    def exec_chrome_case2(self):
        """執行cas2.
        進入home page, 執行case2, 重新loading home page
        """
        try:
            self.driver.get_url(url)
            Case2(Unit(self.driver, Element(self.driver))).exec_case()
            self.log.info("Case2 結束")
        except:
            self.log.warning("Case2 有異常問題")

    def exec_chrome_case3(self):
        """執行cas3.
        進入home page, 執行case3, 重新loading home page
        """
        try:
            self.driver.get_url(url)
            Case3(Unit(self.driver, Element(self.driver))).exec_case()
            self.log.info("Case3 結束")
        except:
            self.log.warning("Case3 有異常問題")
