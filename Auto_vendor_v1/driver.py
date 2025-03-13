import logging.config
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

 
class Driver(webdriver.Remote):

    @property
    def driver(self) -> webdriver.Remote:
        return self.__driver

    def __init__(self):
        """啟動瀏覽器，並設定為手機版模擬"""
        option = Options()
        # 設定模擬手機（iPhone 14）
        mobile_emulation = {
            "deviceMetrics": {
                "width": 390,
                "height": 844,
                "pixelRatio": 3.0,
            },  # iPhone 14 解析度
            # "clientHints": {"platform": "macOS", "mobile": True},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36",
        }

        # 設定模擬手機（Samsung 24）
        # mobile_emulation = {
        #     #
        # }

        option.add_experimental_option("mobileEmulation", mobile_emulation)
        option.add_argument("--window-size=390,844")  # 瀏覽器大小
        # 啟動 Chrome 瀏覽器
        self.__driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=option
        )
        self.__driver.switch_to.window(
            self.__driver.current_window_handle
        )  # 切換到當前視窗
        print(os.path.dirname(__file__))
        logging.config.fileConfig(os.path.dirname(__file__) + "/logging.conf")
        self.logger = logging.getLogger()
        self.logger.warning("234")
        logging.warning("driver 啟動成功2")

    def get_url(self, url: str):
        self.driver.get(url)

    def wait_until_element(self, param, waitTime: float = 5) -> bool:
        try:
            WebDriverWait(self.driver, waitTime).until(EC.presence_of_element_located((By.XPATH, param))) 
            return True
        except TimeoutException:
            if __debug__:
                logging.ERROR(f"等待 Element:{param}超時")
            return False
        except Exception as e:
            if __debug__:
                logging.ERROR(f"Element異常：\r\n{e}")
            return False

    def get_ele_by_xpath(self, param: str) -> WebElement:
        if self.wait_until_element(param):
            return self.driver.find_element(By.XPATH, param)
        else:
            logging.ERROR(f"找不到")
            return None        
