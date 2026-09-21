#Locator Method : Text (get_by_text) 
#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" id="username">
#<button onclick="fillTextbox()">Click Me</button>
#in the above case since text is provided by using button html element we are using that

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")

    page.get_by_text("Click Me").click() #CLick on button - Since text is a button element
    page.get_by_test_id("t1").clear() #Remove the value 

    #above 2 lines indicates both click() and clear are working fine
    page.get_by_text("click me").click #It is not case sensitive
    page.get_by_test_id("t1").clear() #Remove the value 

    page.get_by_text("click").click() #It supports partial match 
    page.get_by_test_id("t1").clear() #Remove the value 

    page.get_by_text("Click Me",exact=True).click() #CLick on button - Since text is a button element
    page.get_by_test_id("t1").clear() #Remove the value 

    #Locator     CaseSensitive(CS)  AllowPartialMatch  HaveExactMatch
    #alt_text     Not CS                Yes               Yes
    #label        Not CS                Yes               Yes 
    #placeholder  Not CS                Yes               Yes 
    #Test Id        CS                   No                No 
    #Text         Not CS                Yes               Yes



