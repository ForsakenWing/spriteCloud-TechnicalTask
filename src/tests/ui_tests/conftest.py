from selenium import webdriver
from selenium.webdriver import ChromeOptions
from . import ClassHelper
import pytest


@pytest.fixture(scope="module", autouse=True)
def driver():
    global _driver
    options = ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # _driver = webdriver.Remote(
    #     command_executor='http://localhost:4444/wd/hub',
    #     options=options
    # )
    _driver = webdriver.Chrome(options=options)
    _driver.maximize_window()
    return _driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        if rep.failed:
            dr = ClassHelper(_driver)
            dr.save_screenshot()


@pytest.fixture(scope="module", autouse=True)
def quit_session(request, driver):
    def fin():
        driver.quit()
    request.addfinalizer(fin)
