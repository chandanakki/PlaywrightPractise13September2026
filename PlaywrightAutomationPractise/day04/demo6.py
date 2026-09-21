#Locator Method : Role (get_by_role) 
#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" id="username">
#When we develop a Custom Webpage Role Was Introduced
#In Dynamic web element we need to identify using tags such as ARIA role 
#(Accessing Rich Internet Application)
#Playwright Supports this using Role Tag
#To find the role of the element we use Playwright Inspector
#- textbox "UserName"   textbox is role and Username is name (In Playwright Insoector)


from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")

    page.get_by_role("textbox").fill("a") #In PLaywright Inspect For Input we got this
    #- textbox "UserName" That is the reason we use role as "textbox"

    page.get_by_role("Textbox").fill("b") #Its not Case Sensitive

    page.get_by_role("textbox",exact=True).fill("d") #Have Exact Match

    page.get_by_role("box").fill("c") #It will not allow Partial Match


    #Locator     CaseSensitive(CS)  AllowPartialMatch  HaveExactMatch
    #alt_text     Not CS                Yes               Yes
    #label        Not CS                Yes               Yes 
    #placeholder  Not CS                Yes               Yes 
    #Test Id        CS                  No                No 
    #Text         Not CS                Yes               Yes
    #Title        Not CS                Yes               Yes
    #Role         Not CS                No                Yes

    


