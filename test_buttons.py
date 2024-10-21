import pytest
from playwright.sync_api import expect, Page


@pytest.fixture(scope="function")  # scope="function" is default
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({"height": 1080, "width": 1920})
    yield page


def test_simple_exists(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/simple")
    button = page.locator("#submit-id-submit")
    expect(button).to_be_visible()


def test_simple_button_click(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/simple")
    button = page.locator("#submit-id-submit")
    button.click()
    result_text = page.locator(".result-text")
    expect(result_text).to_have_text("Submitted")


def test_like_a_button_exists(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    button = page.locator(".a-button")
    expect(button).to_be_visible()


def test_like_a_button_click(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    button = page.locator(".a-button")
    button.click()
    result_text = page.locator(".result-text")
    expect(result_text).to_have_text("Submitted")
