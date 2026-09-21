#https://aksharatraining.com/sample1.html
#In the dev tool bar press Ctrl+F
#In the search box type the XPath
#It will highlight the matching html code in the tree in yellow color
#It will highlight the matching element on the page
#It will display number of matches in below case its matching with one
#We have written the below playwright script using Xpath

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/sample1.html")
    page.locator("xpath=./html/body/a").click()


