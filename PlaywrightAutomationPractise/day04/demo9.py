# Basic Login Script
# url:https://pos.aksharatraining.in/login
# username:student123 password:akshara123
# Format code Shift+Alt+F (Windows Short Cut Key Board)
# Outer HTML Element for UserName
# <input class="form-control" id="input-username" name="username" type="text" placeholder="Username">
# Outer HTML Element for Password
# <input class="form-control" id="input-password" name="password" type="password" placeholder="Password">
# Outer HTML For Go Button
# <button class="btn btn-lg btn-primary" name="login-button" type="submit">Go</button>
# Outer HTML For Logout 
# <a href="https://pos.aksharatraining.in/public/home/logout">Logout</a>
# Explore All Locate Methods

# Login Script For POS App
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:

   # Open The Browser
    browser = playwright.chromium.launch(headless=False)

   # Open a tab(page)
    page=browser.new_page()

   # Enter The URL
    page.goto("https://pos.aksharatraining.in/public/login")

   # Page Title 
    print(page.title())

   # Enter Valid username (student123)
    page.get_by_placeholder("Username").fill("student123")

   # Enter Valid password (akshara123)
    page.get_by_placeholder("Password").fill("akshara123")

   # Click on go button
    page.get_by_text("Go",exact=True).click() #1st preference use exact=true. Then go for first.click()

   # Page Title
    print(page.title())

   # Click on Logout
    page.get_by_text("Logout").click()

    # Page Title
    print(page.title())