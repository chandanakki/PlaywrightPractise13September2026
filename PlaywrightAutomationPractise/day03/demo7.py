from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_alt_text("your name?",exact=True).type("Chandan")
    
    #Strict Mode - Not Case Sensitive and No partial match

    

    