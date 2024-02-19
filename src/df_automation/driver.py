from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class Driver(webdriver.Chrome):
    DRIVER_NAME: str = 'chromedriver.exe'

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        service = Service(self.DRIVER_NAME)

        super(Driver, self).__init__(service=service, options=chrome_options)

    @property
    def driver_path(self):
        return os.path.join(__file__[:__file__.find('src')], self.DRIVER_NAME)
        # return os.path.join(os.path.dirname(os.path.abspath(__file__)), self.DRIVER_NAME)