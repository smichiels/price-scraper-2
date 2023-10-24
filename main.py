import logging
import os

import pandas as pd

from constants import CSV_FILE
from scrapers.amazon import AmazonScraper
from scrapers.coolmod import CoolmodScraper
from scrapers.pcc import PccScraper

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def main():
    df_comp = pd.read_csv(CSV_FILE, index_col="component", sep=";")
    df_prices = pd.DataFrame(columns=df_comp.columns, index=df_comp.index)
    scrapers_dict = {"amazon": AmazonScraper(), "pcc": PccScraper(), "coolmod": CoolmodScraper()}
    for tienda in df_comp.columns:
        df_prices[tienda] = scrapers_dict[tienda].parse_urls(df_comp[tienda].values)
    df_prices.fillna(99999, inplace=True)
    df_build = pd.DataFrame({'store': df_prices.idxmin(axis=1), 'price': df_prices.min(axis=1)})
    logger.info("Best affordable build: ")
    logger.info(df_build)
    if os.environ.get("CHAT_ID") and os.environ.get("TOKEN"):
        print("caca")


if __name__ == "__main__":
    main()
