import logging
import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .exceptions import CustomTimeoutException, CustomNoSuchElementException


class Screenshot:

    def save_screenshot(self, name):
        screenshot_path = f'result/{name}.png'
        self.driver.save_screenshot(screenshot_path)


class ClassHelper(Screenshot):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait_t = 15
        self.wait = WebDriverWait(self.driver, self.wait_t)

    def navigate_to_page(self, url):
        self.driver.get(url)

    def upload_file(self, element, path_to_file):
        by_what, locator = self.divide(element)
        el = self.search_element(by_what, locator)
        el.send_keys(path_to_file)

    def navigate_to_page(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def handle_alert(self):
        try:
            WebDriverWait(
                self.driver, 3
            ).until(
                EC.alert_is_present(),
                'Timed out waiting for PA creation '
                'confirmation popup to appear.'
            )
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            logging.warning("Expected to handle alert")

    @staticmethod
    def divide(element):
        """
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        by_what, locator = element[:element.find('=')], element[element.find('=') + 1:]
        return by_what, locator

    def search_element(self, by_what, locator, one_el=True):
        if one_el:
            locator = self.driver.find_element(by_what, locator)
        else:
            locator = self.driver.find_elements(by_what, locator)
        return locator

    def move_to_el(self, element):
        by_what, locator = self.divide(element)
        el = self.search_element(by_what, locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def check_visible_element(self, element):
        by_what, locator = self.divide(element)
        self.wait.until(EC.visibility_of_element_located((by_what, locator)))

    def check_disappearance_element(self, element):
        by_what, locator = self.divide(element)
        self.wait.until_not(EC.visibility_of_element_located((by_what, locator)))

    def click_on_element(self, element):
        by_what, locator = self.divide(element)
        try:
            self.wait.until(EC.element_to_be_clickable((by_what, locator))).click()
        except TimeoutException:
            raise CustomTimeoutException(f'TimeoutException while clicking element={element}')
        except NoSuchElementException:
            raise CustomNoSuchElementException(f'NoSuchElementException while clicking element={element}')

    def clear_data_in_field(self, element):
        by_what, locator = self.divide(element)
        el = self.wait.until(EC.element_to_be_clickable((by_what, locator)))
        el.clear()

    def set_value(self, element, data):
        by_what, locator = self.divide(element)
        el = self.wait.until(EC.element_to_be_clickable((by_what, locator)))
        try:
            el.clear()
            el.send_keys(data)
        except Exception:
            time.sleep(2)
            el = self.wait.until(EC.element_to_be_clickable((by_what, locator)))
            el.clear()
            el.send_keys(data)

    # For editing List records
    def set_list_value(self, element, data):
        by_what, locator = self.divide(element)
        el = self.wait.until(EC.element_to_be_clickable((by_what, locator)))
        try:
            # el.clear()
            el.send_keys(data)
        except Exception:
            time.sleep(2)
            el = self.wait.until(EC.element_to_be_clickable((by_what, locator)))
            el.clear()
            el.send_keys(data)

    def get_attribute_el(self, element, attribute):
        by_what, locator = self.divide(element)
        try:
            el = self.search_element(by_what, locator)
            att = el.get_attribute(attribute)
        except Exception:
            time.sleep(2)
            el = self.search_element(by_what, locator)
            att = el.get_attribute(attribute)
        return att

    def refresh_browser(self):
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

    def get_text_from_elements(self, element):
        by_what, locator = self.divide(element)
        elements = self.wait.until(EC.presence_of_all_elements_located((by_what, locator)))
        return [i.text for i in elements]

    def get_text_from_element(self, element):
        by_what, locator = self.divide(element)
        el = self.wait.until(EC.visibility_of_element_located((by_what, locator)))
        return el.text
