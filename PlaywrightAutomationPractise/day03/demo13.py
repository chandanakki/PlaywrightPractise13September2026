#<input type="text" placeholder="user name" alt="your name?" data-testid="t1" title="text box" 
# id="username">
#get_by_label label=username

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element2.html")
    page.get_by_label("UserName2").type("A") #Not Case Sensitive Allow Partial Match
    page.get_by_label("username2").type("B")
    page.get_by_label("name2").type("C")
    #page.get_by_label("UserName").type("A") #error Allow PM (Partial Match)
    page.get_by_label("UserName",exact=True).type("X")
    page.get_by_label("user").first.type("X") #Allow Partial 1st One