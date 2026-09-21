#ADA American Disability Act : Disable Persons Should be able to use
#Tab button was introduced
#Colour Blindness Icon Was Introduced
#Screen Reader Is Introduced 
#When we develop a Custom Webpage Role Was Introduced
#In Dynamic web element we need to identify using tags such as ARIA role 
#(Accessing Rich Internet Application)
#Playwright Supports this using Role Tag
#To find the role of the element we use Playwright Inspector
#In Real Time elements are very dynamic

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.pause() #This method will open/invoke Playwright Inspector.
    #(- textbox "UserName":  - /placeholder: user name)



