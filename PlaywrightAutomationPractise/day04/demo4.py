#Locator Method : Title (get_by_title) 
#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" id="username">
#<button onclick="fillTextbox()">Click Me</button>
#in the above case since text is provided by using button html element we are using that

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")

    page.get_by_title("text box").fill("a")

    page.get_by_title("Text Box").fill("b") #Not Case Sensitive

    page.get_by_title("box").fill("c") #Allows Partial Match

    page.get_by_title("text box",exact=True).fill("d") #Exact Is True Option is there
     

    #Locator     CaseSensitive(CS)  AllowPartialMatch  HaveExactMatch
    #alt_text     Not CS                Yes               Yes
    #label        Not CS                Yes               Yes 
    #placeholder  Not CS                Yes               Yes 
    #Test Id        CS                   No                No 
    #Text         Not CS                Yes               Yes
    #Title        Not CS                 Yes              Yes 



