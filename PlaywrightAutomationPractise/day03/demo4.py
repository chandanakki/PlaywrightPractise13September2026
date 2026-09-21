from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    textbox=page.get_by_alt_text("invalid") #it will only note down locator type - it will not find the element
    print(type(textbox))
    print("Done")

    #We get no such element exception in Selenium
    #it will only note down locator type - it will not find
    #this behaviour is for all the locators

    