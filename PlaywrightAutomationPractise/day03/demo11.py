from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_alt_text("your name?").type("Chandan")
    #page.get_by_alt_text("your name?").first.type("Vinutha")
    page.get_by_alt_text("your name?").first.fill("Vinutha")

#In Playwright if we use first type only for one matching element it works
#If we use "first.type" Its not removing existing one
#If we use "first.fill" It overwrites existing one
#Type is locator level method
