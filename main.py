import utils
from constants import CSV_FILE
from scrapers.pcc import PccScraper
from utils import get_minimum_build
from scrapers.amazon import AmazonScraper

import pandas as pd


def main():
    df_comp = pd.read_csv(CSV_FILE, index_col="component", sep=";")
    df_prices = pd.DataFrame(columns=df_comp.columns, index=df_comp.index)
    scrapers_dict = {"amazon": AmazonScraper(), "pcc": PccScraper()}
    for tienda in df_comp.columns:
        df_prices[tienda] = scrapers_dict[tienda].parse_urls(df_comp[tienda].values)
    print(df_prices)


if __name__ == "__main__":
    main()
