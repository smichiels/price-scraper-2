from config.filenames import DEFAULT_JSON_FILENAME
from file_io import json_io
from scrapers import amazon, coolmod, pcc
from utils.component_utils import get_minimum_build


def main():
    try:
        f = input("Filename: ")
    except Exception as exc:
        print(str(exc))
        f = DEFAULT_JSON_FILENAME
    comp_list = json_io.read_json_file(f)
    scraper_list = [amazon.AmazonScraper(comp_list),
                    pcc.PccScraper(comp_list),
                    coolmod.CoolmodScraper(comp_list)]
    for scraper in scraper_list:
        scraper.parse_urls()
    json_io.write_json_file(f, comp_list)
    get_minimum_build(comp_list)

    
main()
