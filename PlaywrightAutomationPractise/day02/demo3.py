from playwright.sync_api import sync_playwright

# # Start the playwright
# playwright = sync_playwright().start()

# # Open the browser
# browser = playwright.firefox.launch(headless=False)

# # Open the page
# page = browser.new_page()

# page.goto("https://www.google.com")

# print(page.title())

# page.close()

# browser.close()

# playwright.stop()

with sync_playwright() as playwright:
    # Open the browser
    browser = playwright.firefox.launch(headless=False)
    # Open the page(tab)
    page = browser.new_page()

    # enter the url
    page.goto("https://www.google.com/")
    print(page.title())
