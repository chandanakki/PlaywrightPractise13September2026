from playwright.sync_api import sync_playwright

#if locator is matching with more than one element , then we can pick 1st one
#we can also pic 2nd , nth...
with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element2.html")
    page.get_by_alt_text("your name?").first.type("Chandan")

    #In Selenium if there are duplicate elements it allows the first one
    #In Playwright 
    #we have option to make it Case Sensitive & Not Case Sensitive
    #we have option to make it Partial Match & Not Partial Match
    #we have option to identify first element or not first element
