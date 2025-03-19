import time

from log_package import Log
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Driver(webdriver.Remote):

    @property
    def driver(self) -> webdriver.Remote:
        return self.__driver

    def __init__(self, mobile, browser=None):
        """啟動瀏覽器，並設定為手機版模擬"""
        self.logger = Log().logger
        match mobile:
            # 設定模擬手機（iPhone 14）
            case "IPhone":
                mobile_emulation = {
                    "deviceMetrics": {
                        "device": "iPhone 14",
                        "width": 390,
                        "height": 844,
                        "pixelRatio": 3,
                    },
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1",
                }
            # 設定模擬手機（Samsung Galaxy S22 ULTRA）
            case "Samsung":
                mobile_emulation = {
                    "deviceMetrics": {
                        "device": "Samsung Galaxy S22 ULTRA - 2022",
                        "width": 360,
                        "height": 772,
                        "dpr": 4,
                        "user_agent": "-",
                    },
                    "userAgent": "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
                }
            case _:
                self.logger.error("裝置選擇錯誤")
        match browser:
            case "Chrome":
                # 啟動 Chrome
                option = ChromeOptions()
                option.add_experimental_option("mobileEmulation", mobile_emulation)
                option.add_argument("--lang=zh-TW")  # 設定成繁體中文
                self.__driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=option,
                )
            case "Edge":
                option = EdgeOptions()
                option.add_experimental_option("mobileEmulation", mobile_emulation)
                option.add_argument("--lang=zh-TW")  # 設定成繁體中文
                self.__driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=option,
                )
            case _:
                self.logger.error("瀏覽器選擇錯誤")
        self.actions = ActionChains(self.driver)
        self.logger.info("driver 啟動成功")

    def get_url(self, url: str):
        """開啟網頁"""
        self.driver.get(url)
        self.logger.info(f"前往 {url}")

    def wait_until_element(self, param, waitTime: float = 5) -> bool:
        """等待元素出現"""
        try:
            WebDriverWait(self.driver, waitTime).until(
                EC.presence_of_element_located((By.XPATH, param))
            )
            return True
        except TimeoutException:
            if __debug__:
                self.logger.error(f"等待 Element:{param}超時")
            return False
        except Exception as e:
            if __debug__:
                self.logger.error(f"Element有其他異常：\r\n{e}")
            return False

    def get_ele_by_xpath(self, param: str) -> WebElement:
        """根據xpath取得元素"""
        if self.wait_until_element(param):
            return self.driver.find_element(By.XPATH, param)
        else:
            self.logger.error(f"找不到該元素")
            return None

    def get_elements_by_xpath(self, element: WebElement, s_param: str) -> WebElement:
        """根據xpath取得元素的子元素們"""
        try:
            e = self.driver if element == None else element
            WebDriverWait(e, 5).until(
                EC.presence_of_element_located((By.XPATH, s_param))
            )
            return e.find_elements(By.XPATH, s_param)
        except TimeoutError:
            self.logger.error(f"找不到該 {element} 元素的子元素 {s_param}")
            return None

    def element_click(self, element: WebElement):
        """點擊元素"""
        element.click()
        time.sleep(0.5)  # 等待元素反應

    def screen_shot(self, path: str):
        """截圖"""
        self.driver.save_screenshot(path)
        self.logger.info("截圖成功")

    def scroll_to_element(self, element):
        """滾動到指定元素"""
        self.actions.move_to_element(element).perform()
