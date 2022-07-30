import time

import pytest

from . import ClassHelper


def save_screenshot(func):
    def wrapper(self, request):
        name = request.node.name
        func(self, request)
        if self.get_test_result():
            self.dr.save_screenshot(f'passed_{name}')

    return wrapper


class Common:

    def __init__(self):
        self._fail = ''

    def is_failed(self, fail):
        if self._fail != '':
            pytest.fail(fail)

    def fail(self, fail):
        if type(fail) != str:
            fail = [str(x) for x in fail]
            fail = ' '.join(fail)
        self._fail += '\n' + fail


class CommonBrowser(Common):

    def __init__(self, driver):
        super().__init__()
        self.dr = ClassHelper(driver)
        self.date_start_tests = int(time.time())


class Browser(CommonBrowser):

    def __init__(self, driver):
        super().__init__(driver)
        self.dr = ClassHelper(driver)

    def get_test_result(self):
        return False if self._fail != '' else True

    def open_page(self, domain):
        self.dr.navigate_to_page(f"https://{domain}")

    def handle_alert(self):
        self.dr.handle_alert()

    def nav_to_click_playground(self):
        self.dr.click_on_element('xpath=//a[@href="/click"]')

    def nav_to_class_attr_playground(self):
        self.dr.click_on_element('xpath=//a[@href="/classattr"]')

    def nav_to_dynamic_id_playground(self):
        self.dr.click_on_element('xpath=//a[@href="/dynamicid"]')

    @save_screenshot
    def click_on_bad_button(self, request):
        self.dr.click_on_element('xpath=//button[@id="badButton"]')
        time.sleep(1)

    @save_screenshot
    def click_on_blue_btn(self, request):
        self.dr.click_on_element(
            'xpath=//button['
            'contains(concat(" ",normalize-space(@class)," ")," btn-primary ")]',
        )
        self.handle_alert()

    @save_screenshot
    def click_on_btn_with_dynamic_id(self, request):
        self.dr.click_on_element('xpath=//button[contains(text(), "Button with Dynamic ID")]')
