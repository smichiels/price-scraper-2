from time import sleep
import requests

from lxml import html

from scrapers.scraper import GenericScraper
from config.xpath_routes import PCC_XPATH_PRICE


class PccScraper(GenericScraper):

    def __init__(self, object_list):
        super().__init__(object_list, "pcc")

    def parse_urls(self):
        for obj in self.object_list:
            url = f'https://www.pccomponentes.com/{obj["ids"]["pcc_id"]}/'
            headers = {'User-Agent': 'Magic Browser'}
            try:
                page = requests.get(url, headers=headers)
                if page.status_code != 200:
                    raise ValueError(f'Error in web request - PCC - Product {obj["name"]} - {page.status_code}')
                sleep(1)
                doc = html.fromstring(page.content)
                new_price = float(doc.xpath(PCC_XPATH_PRICE)[0].attrib["data-baseprice"])
                self.update_price(obj, new_price)
            except IndexError as e:
                print(f"Problem getting PCC price of {obj['name']}, please check manually")
            except ValueError as e:
                print(str(e))
