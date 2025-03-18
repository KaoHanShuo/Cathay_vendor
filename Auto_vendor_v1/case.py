from driver import Driver
from element import *
from unit import *
from parameter import *
import time


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
        self.log.info(f"信用卡的數量為{card_num}")


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
        for i in range(1,self.unit.unit_cardIntroducePage.count_pagination_bullets()):
            self.unit.unit_homePage.screen_shot_home(pic_folder + f"/case3 - {i}.png")
            self.unit.unit_cardIntroducePage.click_pagination_bullets(i)
        time.sleep(3)
class AutoTest(object):
    def __init__(self):
        self.driver = Driver()

    def exec_chrome_case1(self):
        """執行cas1.
        進入home page, 執行case1, 重新loading home page
        """
        try:
            self.driver.get_url(url)
            Case1(Unit(self.driver, Element(self.driver))).exec_case()
        except:
            pass
        finally: 
            self.driver.get_url(url)

    def exec_chrome_case2(self):
        """執行cas2.
        進入home page, 執行case2, 重新loading home page
        """
        try:
            self.driver.get_url(url)
            Case2(Unit(self.driver, Element(self.driver))).exec_case()
        except:
            pass
        finally: 
            self.driver.get_url(url)
    def exec_chrome_case3(self):
        """執行cas3.
        進入home page, 執行case3, 重新loading home page
        """
        self.driver.get_url(url)
        Case3(Unit(self.driver, Element(self.driver))).exec_case()
        # try:
        #     self.driver.get_url(url)
        #     Case3(Unit(self.driver, Element(self.driver))).exec_case()
        # except:
        #     pass
        # finally: 
        #     self.driver.get_url(url)