import pytest
from playwright.sync_api import sync_playwright
import allure

@allure.title("Login Success Test")
def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.rahulshettyacademy.com/loginpagePractise/")
        page.get_by_label("Username:").fill("rahulshettyacademy")
        page.get_by_label("Password:").fill("learning")
        page.get_by_role("combobox").select_option("teach")
        page.locator("#terms").check()
        page.fill("#password", "demo_pass")

        page.click("#login")
        allure.attach(page.screenshot(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        assert page.url.endswith("/dashboard")
        browser.close()
