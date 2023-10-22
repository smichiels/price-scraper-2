import pandas as pd

from scrapers.amazon import AmazonScraper
from scrapers.coolmod import CoolmodScraper
from scrapers.pcc import PccScraper

CSV_FILE = "./components.csv"




def main():
    df_comp = pd.read_csv(CSV_FILE, index_col="component", sep=";")
    df_prices = pd.DataFrame(columns=df_comp.columns, index=df_comp.index)
    scrapers_dict = {"amazon": AmazonScraper(), "pcc": PccScraper(), "coolmod": CoolmodScraper()}
    for tienda in df_comp.columns:
        df_prices[tienda] = scrapers_dict[tienda].parse_urls(df_comp[tienda].values)
    print(df_prices)


if __name__ == "__main__":
    main()
