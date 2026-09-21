#Locator Method : Test Id (get_by_test_id) is data-test_id only we cant use html element test_id
#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" id="username">
#In web element it will be data-testid="t1"
#This is added by developer to test it. Usually in Production it will not be present

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_test_id("t1").fill("apple")
    page.get_by_test_id("T1").fill("mango") # It is Case Sensitive
    page.get_by_placeholder("user").fill("orange") #It will not allow Partial Match 
    #page.get_by_placeholder("user name",exact=True).fill("Guava")#Exact Option is not there as By default test id is exact match


   #Locator     CaseSensitive  AllowPartialMatch  HaveExactMatch
    #alt_text     Not CS          Yes               Yes
    #label        Not CS          Yes               Yes 
    #placeholder  Not CS          Yes               Yes 
    #Test Id        CS             No                No 