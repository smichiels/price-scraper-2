from time import sleep

import requests
from lxml import html

from config.xpath_routes import COOLMOD_XPATH_PRICE
from scrapers.scraper import GenericScraper


class CoolmodScraper(GenericScraper):

    def __init__(self, object_list):
        super().__init__(object_list, "coolmod")

    def parse_urls(self):
        for obj in self.object_list:
            url = f'http://www.coolmod.com/{obj["ids"]["coolmod_id"]}/'
            headers = {'User-Agent': 'Magic Browser'}
            try:
                page = requests.get(url, headers=headers)
                if page.status_code != 200:
                    raise ValueError(f'Error in web request - Coolmod - Product {obj["name"]} - {page.status_code}')
                sleep(1)
                doc = html.fromstring(page.content)
                new_price = float(doc.xpath(COOLMOD_XPATH_PRICE)[0].replace('€', '').replace(',','.').strip())
                self.update_price(obj, new_price)
            except IndexError as e:
                print(f"Problem getting Coolmod price of {obj['name']}, please check manually")
            except ValueError as e:
                print(str(e))
