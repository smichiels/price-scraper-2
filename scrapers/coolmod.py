import logging

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class CoolmodScraper:
    @staticmethod
    def get_coolmod_price(url):
        if pd.isna(url):
            return None
        headers = {"User-Agent": "Magic Browser"}
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()
                soup = bs(response.content, "lxml")
                price_element = soup.find(class_="fixedbuybtnfinalprice")
                if price_element:
                    price_text = price_element.get_text().replace(",", ".").replace("€", "")
                    logger.info(f"Parsed price {price_text} - {url}")
                    return float(price_text)
            logger.info(f"No price found - {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.exception(f"Error en la solicitud web {url}: {e}")
            return None
        except Exception as e:
            logger.exception(f"Error al obtener el precio de Coolmod para {url}: {e}")
            return None

    def parse_urls(self, urls):
        result = [self.get_coolmod_price(url) for url in urls]
        return result
