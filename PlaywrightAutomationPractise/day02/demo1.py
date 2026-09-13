from playwright.sync_api import sync_playwright

#Start the playwrigh
playwright = sync_playwright().start()

#Open the browser
browser = playwright.firefox.launch(headless=False)

#Open the page 
page = browser.new_page()

page.goto("https://www.google.com")

print(page.title())

page.close()

browser.close()

playwright.stop()



