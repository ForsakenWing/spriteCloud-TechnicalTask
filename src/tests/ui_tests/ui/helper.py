from selenium.webdriver.support.ui import WebDriverWait


class Screenshot:

    def save_screenshot(self):
        screenshot_path = 'logs/failed.png'
        self.driver.save_screenshot(screenshot_path)


class ClassHelper(Screenshot):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait_t = 15
        self.wait = WebDriverWait(self.driver, self.wait_t)

    def navigate_to_page(self, url):
        self.driver.get(url)
