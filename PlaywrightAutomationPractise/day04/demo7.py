#To find the role of the element we use Playwright Inspector
#- textbox "UserName"   textbox is role and Username is name (In Playwright Insoector)
#exact option is for name (and not for role)

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")

    page.get_by_role("textbox",name="UserName").fill("a") #Role is mandatory argument and name is optional argument used for filtering purpose

    page.get_by_role("textbox",name="userName").fill("b")

    page.get_by_role("textbox",name="user").fill("c")

    #page.get_by_role("textbox",name="user",exact="True").fill("d") #exact option is for name (and not for role)

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
