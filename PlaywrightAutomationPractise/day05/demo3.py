#https://aksharatraining.com/sample2.html
#HTML Tree Right Click On HTML Code Copy Select Option Copy Full XPATH
#/html/body/a[1]
#Since there are multiple elements matching with the XPath we get Error: strict mode violation: locator("xpath=./html/body/a") resolved to 3 elements:
#How to handle this in XPath -- In Xpath we can use Indexing such as a[1]
#In XPath index always starts from 1 not from 0(Zero)
#Xpath is Xpath irrespective of any Test Automation Tool these are options provided by browser
#Test Automation Tools Interact With Send request with broswer --Send with XPath-- It will give address -- This interacts with DOM
#If we dont specify index it means all the HTML 
#/html --All HTML Within Root
#html/body/a --All the a within body

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=2000)
    page=browser.new_page()
    page.goto("https://aksharatraining.com/sample2.html")
    #page.locator("xpath=./html/body/a").click() #--multiple elements matching with the XPath 
    page.locator("xpath=/html/body/a[1]").click()
    page.go_back()

    page.locator("xpath=/html/body/a[2]").click()
    page.go_back

    page.locator("xpath=/html/body/a[3]").click()
    page.go_back