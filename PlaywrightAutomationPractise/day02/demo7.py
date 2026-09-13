import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://google.com")
    page.set_viewport_size({"width":500,"height":500})
    time.sleep(6)