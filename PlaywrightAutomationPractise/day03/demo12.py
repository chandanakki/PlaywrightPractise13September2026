#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" 
# id="username">
#get_by_label label=username

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    page.get_by_label("UserName").type("Chandan")
    page.get_by_label("username").type("Vinutha") #By default it is not case sensitive
    page.get_by_label("ser").type("Vinutha") #Allow Partial Match
    page.get_by_label("UserName",exact=True).fill("Chandu")
    page.get_by_label("username",exact=True).fill("ChanduBhai") #error Time Out Error