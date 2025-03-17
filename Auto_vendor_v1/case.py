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
        self.unit.unit_homePage.click_hamburger_menu()


class Case2(object):
    """點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖"""


class Case3(object):
    """個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖"""

class AutoTest(object):
    def __init__(self):
        self.driver = Driver()
        self.driver.get_url(url)
    
    def exec_chrome_case1(self):
        Case1(Unit(self.driver, Element(self.driver))).exec_case()

    def exec_chrome_case2(self):
        Case2(Unit(self.driver, Element(self.driver))).exec_case()

    def exec_chrome_case3(self):
        Case3(Unit(self.driver, Element(self.driver))).exec_case()