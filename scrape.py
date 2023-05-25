import os
from dotenv import load_dotenv
import asyncio
from playwright.async_api import async_playwright

load_dotenv()  # take environment variables from .env.

account_id = os.getenv('ACCOUNT_ID')
zone_name = os.getenv('ZONE_NAME')
password = os.getenv('PASSWORD')

auth = f'brd-customer-{account_id}-zone-{zone_name}:{password}'
browser_url = f'https://{auth}@zproxy.lum-superproxy.io:9222'

async def main():
    async with async_playwright() as pw:
        print('connecting')
        browser = await pw.chromium.connect_over_cdp(browser_url)
        print('connected')
        page = await browser.new_page()
        print('goto')
        await page.goto('https://example.com', timeout=120000)
        # print('done, evaluating')
        # print(await page.evaluate('()=>document.documentElement.outerHTML'))
        await browser.close()

asyncio.run(main())
