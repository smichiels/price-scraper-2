from time import sleep
import requests

from lxml import html

from config.xpath_routes import COOLMOD_XPATH_PRICE

class CoolmodParser():
    def __init__(self, object_list):
        self.object_list = object_list

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
                if obj["prices"]["coolmod_price"] is not None:
                    obj["prices"]["last_coolmod_price"] =  obj["prices"]["coolmod_price"] 
                else:
                    obj["prices"]["last_coolmod_price"] = new_price
                obj["prices"]["coolmod_price"] = new_price
            except IndexError as e:
                print(f"Problem getting Coolmod price of {obj['name']}, please check manually")
            except ValueError as e:
                print(str(e))
