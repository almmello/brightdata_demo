import os
from dotenv import load_dotenv
import asyncio
from playwright.async_api import async_playwright

load_dotenv()  # take environment variables from .env.

# should look like 'brd-customer-<ACCOUNT ID>-zone-<ZONE NAME>:<PASSWORD>'
account_id = os.getenv('ACCOUNT_ID')
zone_name = os.getenv('ZONE_NAME')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')

auth = f'brd-customer-{account_id}-zone-{zone_name}:{password}'
browser_url = f'https://{auth}@{host}'

async def main():
    async with async_playwright() as pw:
        print('connecting')
        browser = await pw.chromium.connect_over_cdp(browser_url)
        print('connected')
        page = await browser.new_page()
        print('goto')
        await page.goto('https://almmello.com', timeout=120000)
        print('done, evaluating')
        html_content = await page.evaluate('()=>document.documentElement.outerHTML')
        with open('output.html', 'w') as f:
            f.write(html_content)
        await browser.close()

asyncio.run(main())
