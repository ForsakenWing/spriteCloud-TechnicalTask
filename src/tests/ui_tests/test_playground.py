from . import Browser


class TestPlayground:

    def test_button_that_ignores_dom_click_event(self, driver):
        browser = Browser(driver)
        browser.open_page('google.com')
        browser._fail = "aboba"
        browser.isFailed(browser._fail)

    def test_for_defining_correct_button_among_buttons_with_similar_classes(self, driver):
        browser = Browser(driver)
        browser.isFailed(browser._fail)

    def test_for_defining_button_with_dynamic_id(self, driver):
        browser = Browser(driver)
        browser.isFailed(browser._fail)
