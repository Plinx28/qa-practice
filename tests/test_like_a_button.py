from playwright.sync_api import Page

from pages.like_a_button_page import LikeAButtonPage


def test_simple_exists(page: Page):
    simple_page = LikeAButtonPage(page)
    simple_page.open()
    simple_page.check_button_exists()


def test_simple_button_click(page: Page):
    simple_page = LikeAButtonPage(page)
    simple_page.open()
    simple_page.click_button()
    simple_page.check_result_text_is_("Submitted")
