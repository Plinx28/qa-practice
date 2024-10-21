from playwright.sync_api import expect, Locator

from pages.base_page import BasePage

BUTTON_SELECTOR = ".a-button"
RESULT_TEXT_SELECTOR = ".result-text"


class LikeAButtonPage(BasePage):
    url = "https://www.qa-practice.com/elements/button/like_a_button"

    def _find_button(self) -> Locator:
        return self.page.locator(BUTTON_SELECTOR)

    def click_button(self):
        self.page.locator(BUTTON_SELECTOR).click()

    def check_button_exists(self):
        button = self._find_button()
        expect(button).to_be_visible()

    def check_result_text_is_(self, text):
        result_text = self.page.locator(RESULT_TEXT_SELECTOR)
        expect(result_text).to_have_text(text)
