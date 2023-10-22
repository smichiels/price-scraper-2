import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class AmazonScraper:

    @staticmethod
    def get_amazon_price(url):
        if pd.isna(url):
            return None
        headers = {'User-Agent': 'Magic Browser'}
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()
                soup = bs(response.content, "lxml")

                seller_element = soup.find(id='sellerProfileTriggerId')
                if seller_element:
                    logger.info(f"No price for seller Amazon - {url}")
                    return None

                price_element = soup.find(class_='a-price-whole')
                if price_element:
                    price_text = price_element.get_text().replace(',', '')
                    decimal_element = soup.find(class_='a-price-fraction')
                    if decimal_element:
                        price_text += '.' + decimal_element.get_text()
                    logger.info(f"Parsed price {price_text} - {url}")
                    return float(price_text)
                logger.info(f"No price found - {url}")
                return None

        except requests.exceptions.RequestException as e:
            logger.exception(f"Error en la solicitud web {url}: {e}")
            return None
        except Exception as e:
            logger.exception(f"Error al obtener el precio de Amazon para {url}: {e}")
            return None

    def parse_urls(self, urls):
        result = [self.get_amazon_price(url) for url in urls]
        return result
