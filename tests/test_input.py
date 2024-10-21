import pytest
from playwright.sync_api import Page, expect


URL = "https://www.qa-practice.com/elements/input/simple"


def __fill_and_enter(page: Page, valid_text: str):
    text_form = page.get_by_role("textbox")
    text_form.fill(value=valid_text)
    expect(text_form).to_be_visible()
    text_form.press("Enter")


@pytest.mark.parametrize("valid_text", ["22", "333", "s" * 24, "s" * 25])
def test_form_valid(page: Page, valid_text):
    page.goto(URL)
    __fill_and_enter(page, valid_text)
    
    result = page.locator("[class='result-text'][id='result-text']")
    expect(result).to_have_text(valid_text)


@pytest.mark.parametrize("invalid_text", ["", "1", "s" * 26, "слова на русском"])
def test_form_invalid(page: Page, invalid_text):
    page.goto(URL)
    __fill_and_enter(page, invalid_text)
    
    print("It's not OK, just trust me")
    