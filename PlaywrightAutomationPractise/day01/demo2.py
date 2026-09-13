#import
from playwright.sync_api import sync_playwright  # type: ignore[reportMissingImports]

#start the playwright
playwright =sync_playwright().start()

#Open the browser
browser = playwright.chromium.launch()  #headlessMode

#Open the page(tab)
page = browser.new_page()

#enter the url
page.goto("https://www.google.com/")
print(page.title())

#Close the page
page.close()

#Close the browser
browser.close

#Close Playwright
playwright.stop()