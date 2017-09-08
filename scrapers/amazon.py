from time import sleep
import requests

from lxml import html

from config.xpath_routes import AMAZON_XPATH_PRICE

class AmazonParser():
    def __init__(self, object_list):
        self.object_list = object_list

    def parse_urls(self):
        for obj in self.object_list:
            url = f'https://www.amazon.es/dp/{obj["ids"]["amazon_id"]}/'
            headers = {'User-Agent': 'Magic Browser'}
            try:
                page = requests.get(url, headers=headers)
                if page.status_code != 200:
                    raise ValueError(f'Error in web request - Amazon - Product {obj["name"]} - {page.status_code}')
                sleep(1)
                doc = html.fromstring(page.content)
                new_price = float(doc.xpath(AMAZON_XPATH_PRICE)[0].replace('EUR', '').replace(',','.').strip())
                if obj["prices"]["amazon_price"] is not None:
                    obj["prices"]["last_amazon_price"] =  obj["prices"]["amazon_price"]
                else:
                    obj["prices"]["last_amazon_price"] = new_price
                obj["prices"]["amazon_price"] = new_price
            except IndexError as e:
                print(f"Problem getting Amazon price of {obj['name']}, please check manually")
            except ValueError as e:
                print(str(e))
