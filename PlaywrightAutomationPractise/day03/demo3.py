from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=0)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_alt_text("invalid").type("Chandan")

    #it keep on searcing finding the element. 
    #we get Time Out Error : TimeoutError: Locator.type: Timeout 30000ms exceeded
    #we got this error while performing type action
    #it will retry for 30 Seconds
    #even after 30 seconds it is not there it will throw Time Out error