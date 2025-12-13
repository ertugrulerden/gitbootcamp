from patchright.async_api import async_playwright  # pyright: ignore[reportMissingImports]
import asyncio


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str("browser_data"),
            headless=False)
        page = await context.new_page()
        
        await page.goto('https://www.github.com', wait_until='domcontentloaded')


        input("enter to close browser: ")
        await browser.close()


asyncio.run(main())






