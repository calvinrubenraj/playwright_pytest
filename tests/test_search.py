import pytest
from playwright.sync_api import sync_playwright
import allure

@allure.title("Search Feature Test")
def test_search_feature():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wikipedia.org")
        page.fill("input[name='search']", "Playwright")
        page.press("input[name='search']", "Enter")
        allure.attach(page.screenshot(), name="search_result", attachment_type=allure.attachment_type.PNG)
        assert "Playwright" in page.title()
        browser.close()
