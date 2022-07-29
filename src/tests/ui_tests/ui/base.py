from .helper import ClassHelper
import time
import pytest


class Common:

    def __init__(self):
        self._fail = ''

    def isFailed(self, fail):
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

    def open_page(self, domain):
        self.dr.navigate_to_page(f"https://{domain}")
