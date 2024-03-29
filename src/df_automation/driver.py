from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # This package automatically downloads and installs the latest ChromeDriver

class Driver:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)
        chrome_options.add_argument('--log-level=3')  # Set log level to suppress unnecessary warnings

        # Use ChromeDriverManager to automatically download and install the latest ChromeDriver
        service = Service(ChromeDriverManager().install())

        # Initialize Chrome WebDriver with configured options and service
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get(self, link: str):
        self.driver.get(link)

    def find_element(self, *args, **kwargs):
        return self.driver.find_element(*args, **kwargs)

    def find_elements(self, *args, **kwargs):
        return self.driver.find_elements(*args, **kwargs)
    
    def quit(self): 
        self.driver.quit()
