import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    time.sleep(2)
    #Locator Method 1 Get element by alt text and store it in a element textbox
    textbox=page.get_by_alt_text("your name?")
    print(type(textbox)) #Locator --> In selenium it is called as WebElement
    textbox.type("chandan")
    time.sleep(2)