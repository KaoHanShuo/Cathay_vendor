from driver import Driver
from element import *


class UnitHomePage(object):

    def __init__(self, driver: Driver, element: HomePage):
        self.driver = driver
        self.element = element
        self.log = self.driver.logger

    def click_hamburger_menu(self):
        self.driver.element_click(self.element.hamburger_menu)
        self.log.info("點擊左上功能列")


class Unit(object):

    def __init__(self, driver: Driver, element: Element):
        self.driver = driver
        self._unit_homePage = UnitHomePage(driver, element.homePage)

    @property
    def unit_homePage(self):
        return self._unit_homePage
