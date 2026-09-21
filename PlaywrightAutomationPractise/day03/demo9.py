from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element2.html")
    page.get_by_alt_text("your name?").type("Chandan")

#Duplicate Match (locator Element)
#In Selenium first element will match
#Error: strict mode violation: get_by_alt_text("your name?") resolved to 2 elements:

#If Playwright is not able to locate element we will get Time Out error

    

    