# Locator : Get_By_Placeholder

# https://aksharatraining.com/element.html

#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" id="username">

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_placeholder("user name").fill("apple")
    page.get_by_placeholder("User Name").fill("mango") # Not Case Sensitive
    page.get_by_placeholder("user").fill("orange") #Allow Partial Match 
    page.get_by_placeholder("user name",exact=True).fill("Guava")#Have Exact Option

    #If it matces more than one element Strict Model Violation
    #Fill Method : Clear + Type

    #Locator     CaseSensitive  AllowPartialMatch  HaveExactMatch
    #alt_text     Not CS          Yes               Yes
    #label        Not CS          Yes               Yes 
    #placeholder  Not CS          Yes               Yes 
    