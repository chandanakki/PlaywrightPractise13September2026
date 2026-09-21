#While writing the XPath mentioning dot (.) is not manadatory
#The below one is Complete XPath / Full XPath /Absolute XPath
#It is not case sensitive

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/sample1.html")
    #page.locator("xpath=/html/body/a").click()
    #Specifiying dot is not manadatory
    page.locator("xpath=/HTML/BODY/A").click #Complete XPath / Full Path /Absolute XPath
    #It is not case sensitive