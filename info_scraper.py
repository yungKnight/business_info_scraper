import pytest
from playwright.async_api import async_playwright
import asyncio
import scrapy
from scrapy.http import HtmlResponse
import json
import os
import re

@pytest.mark.asyncio
async def test_main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        state = "alaska"  # Set the state to "alaska"
        folder = "collection"
        os.makedirs(folder, exist_ok=True)  # Create a folder for the collection if it doesn't exist

        page_number = 0  # Start from page 1

        while True:
            page = await browser.new_page()

            url = f'https://christianlist.gdirect.com/search-results?BusinessDirectoryId=f3830fa2-22d3-4465-80b2-e1a797dbd0c0&adId=0&IsExpandedSearch=False&CurrentPageNumber={page_number}&ItemsPerPage=50&CategoryId=&Lat=31.9685988&Lng=-99.9018131&SearchTerm=&Distance=0&Address={state}'
            await page.goto(url, timeout=80000)

            await page.wait_for_selector('div.feature')

            businesses = await page.query_selector_all('div.feature')
            client_info = []

            for business in businesses:
                button = await business.query_selector('div.row div.company div.hide-group div.hide-group-button-container.hidden-xs a.btn.btn-xs')
                if button:
                    await button.click()
                    await page.wait_for_selector('div.hide-content')
                else:
                    print('No clickable element found to display full details')
                    continue

                html_content = await page.content()

                response = HtmlResponse(url=page.url, body=html_content.encode(), encoding='utf-8')

                for business in response.css('div.feature'):
                    address = business.css('address').xpath('string()').get().strip()
                    address = re.sub(r'\s+', ' ', address)
                    info = {
                        'address': address,
                        'category': business.css('h5.ntm::text').get(),
                        'name': business.css('h5.ntm.nbm:nth-child(2)::text').get(),
                        'owner': business.css('div.company div.name::text').get(),
                        'operations': business.css('div.description::text').get(), 
                        'phone': '*** hidden by scraper ***',
                        'mail': '*** hidden by scraper ***',
                        'website': business.css('div.website a::text').get()
                    }
                    client_info.append(info)