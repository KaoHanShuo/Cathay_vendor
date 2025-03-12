import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from .Module import *

class Base(object):
    @pytest.fixture
    def driver(self):
        """啟動瀏覽器，並設定為手機版模擬"""
        option = Options()
        # 設定模擬手機（iPhone 14）
        mobile_emulation = {
            "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3.0},  # iPhone 14 解析度
            # "clientHints": {"platform": "macOS", "mobile": True},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36"
        }

        # 設定模擬手機（Samsung 24）
        # mobile_emulation = {
        #     # 
        # }

        option.add_experimental_option("mobileEmulation", mobile_emulation)
        # 啟動 Chrome 瀏覽器
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
        driver.maximize_window()  # 最大化視窗
        driver.switch_to.window(driver.current_window_handle)  # 切換到當前視窗
        yield   
        driver.quit()  # 關閉瀏覽器


class action(object):
    pass