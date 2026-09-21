import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #slow_mo Slows down the application For every line it waits 2000 milli seconds = 2 seconds
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    #browser=playwright.chromium.launch(headless=False,slow_mo=0)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/element.html")
    #Locator Method 1 Get element by alt text and store it in a element textbox
    #textbox=page.get_by_alt_text("your name?")
    #textbox.type("chandan")
    #Code Optimisation Instead of above 2 lines we can write 1 line code
    page.get_by_alt_text("your name?").type("Chandan")