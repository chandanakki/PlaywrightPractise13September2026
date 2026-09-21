from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element2.html")
    page.get_by_alt_text("Your name?",exact=True).type("Chandan")

    #Error: strict mode violation: get_by_alt_text("your name?") resolved to 2 elements
    
    
    

    