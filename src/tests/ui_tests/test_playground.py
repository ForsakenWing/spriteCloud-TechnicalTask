import pytest

from . import Browser


@pytest.fixture(autouse=True, scope="function")
def _prepare_function(driver):
    Browser(driver).open_page('uitestingplayground.com')


class TestPlayground:

    def test_button_that_ignores_dom_click_event(self, driver, request):
        browser = Browser(driver)
        browser.nav_to_click_playground()
        browser.click_on_bad_button(request)

    def test_for_defining_correct_button_among_buttons_with_similar_classes(self, driver, request):
        browser = Browser(driver)
        browser.nav_to_class_attr_playground()
        browser.click_on_blue_btn(request)

    def test_for_defining_button_with_dynamic_id(self, driver, request):
        browser = Browser(driver)
        browser.nav_to_dynamic_id_playground()
        browser.click_on_btn_with_dynamic_id(request)

