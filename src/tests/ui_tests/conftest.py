import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from . import ClassHelper


@pytest.fixture(scope="module", autouse=True)
def driver():
    global _driver
    options = ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # _driver = webdriver.Chrome(options=options)
    _driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    _driver.maximize_window()
    return _driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        if rep.failed:
            dr = ClassHelper(_driver)
            name = item.name
            dr.save_screenshot(f'failed_{name}')


@pytest.fixture(scope="module", autouse=True)
def quit_session(request, driver):
    def fin():
        driver.quit()

    request.addfinalizer(fin)
