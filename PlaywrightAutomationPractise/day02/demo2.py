from playwright.async_api import async_playwright
import asyncio


async def script1():
    # Start the playwright
    playwright = await async_playwright().start()

    # Open the browser
    browser = await playwright.firefox.launch(headless=False)

    # Open the page
    page = await browser.new_page()

    await page.goto("https://www.google.com")

    print(await page.title())

    await page.close()

    await browser.close()

    await playwright.stop()

asyncio.run(script1())
