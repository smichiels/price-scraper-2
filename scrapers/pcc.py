import logging
from datetime import datetime

import pandas as pd
import pytz
import requests
from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class PccScraper:
    @staticmethod
    def get_pcc_price(url):
        if pd.isna(url):
            return None
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
        base_url = "https://webcache.googleusercontent.com/search?q=cache:"
        try:
            with requests.Session() as session:
                response = session.get(base_url + url, headers=headers)
                response.raise_for_status()
                soup = bs(response.content, "lxml")
                price_element = soup.find(id="pdp-price-current-integer")
                if price_element:
                    price_text = price_element.get_text().replace("€", "").replace(",", ".")
                    text_element = soup.find(
                        text=lambda text: "Se trata de una captura de pantalla de la página tal como esta se mostraba el"
                        in text
                    )
                    if text_element:
                        fecha_texto = text_element.split("el ")[1].strip(".")
                        fecha_obj = datetime.strptime(fecha_texto, "%d %b %Y %H:%M:%S %Z")
                        fecha_obj = pytz.utc.localize(fecha_obj)
                        fecha_madrid = fecha_obj.astimezone(pytz.timezone("Europe/Madrid"))
                        logger.info(
                            f"Parsed price {price_text} from caché obtained in {fecha_madrid.strftime('%d/%m/%Y %H:%M')} - {url}"
                        )
                        return float(price_text)
                logger.info(f"No price found - {url}")
                return None
        except requests.exceptions.RequestException as e:
            logger.exception(f"Error en la solicitud web {url}: {e}")
            return None
        except Exception as e:
            logger.exception(f"Error al obtener el precio de PCC para {url}: {e}")
            return None

    def parse_urls(self, urls):
        result = [self.get_pcc_price(url) for url in urls]
        return result
