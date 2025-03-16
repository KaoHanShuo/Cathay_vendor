from case import *
from Unit import Unit
from driver import Driver
from element import Element

if __name__ == "__main__":
    driver = Driver()
    Case1(Unit(driver, Element(driver))).exec_case()
