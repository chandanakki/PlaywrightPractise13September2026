from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.webkit.launch(headless=False)
    page=browser.new_page()
    page.goto("http://google.com")
    print(page.title())
    