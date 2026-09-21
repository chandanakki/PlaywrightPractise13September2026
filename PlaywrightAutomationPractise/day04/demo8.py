#Locator -- Text
#We are passing Locator as Text
#Is it mandatory operation for locator --text = Click Me option
#Ans:Since within locator has multiple methods
#In 2 places Locator Autodetects

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")

    page.get_by_text("Click Me").click()
    page.get_by_test_id("t1").clear()

    page.locator("text=Click Me").click()
    page.get_by_test_id("t1").clear()

    page.locator("text=click me").click() #Not Case Sensitive
    page.get_by_test_id("t1").clear()

    page.locator("text=Click").click()  #Allow Partial Match
    page.get_by_test_id("t1").clear()

    page.locator("text='Click Me'").click()  #Exact Match when we put in single quotes 'Click Me'
    page.get_by_test_id("t1").clear()


#Locator     CaseSensitive(CS)  AllowPartialMatch  HaveExactMatch
#alt_text     Not CS                Yes               Yes
#label        Not CS                Yes               Yes 
#placeholder  Not CS                Yes               Yes 
#Test Id        CS                  No                No 
#Text         Not CS                Yes               Yes
#Title        Not CS                Yes               Yes
#==============================================================
#Role         Not CS                No                ---
#Role_name    Not CS                Yes               Yes
#=============================================================
#Locator(Text) Not CS               Yes                Yes