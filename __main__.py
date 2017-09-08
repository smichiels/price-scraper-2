from config.filenames import DEFAULT_JSON_FILENAME
from file_io import json_io
from scrapers import amazon, coolmod, pcc
from utils.component_utils import get_minimum_build

def main():
    comp_list = json_io.read_json_file(DEFAULT_JSON_FILENAME)
    scraper_list = [amazon.AmazonParser(comp_list),
                    pcc.PccParser(comp_list),
                    coolmod.CoolmodParser(comp_list)]
    for scraper in scraper_list:
        scraper.parse_urls()
    json_io.write_json_file(DEFAULT_JSON_FILENAME, comp_list)
    get_minimum_build(comp_list)

if __name__ == "__main__":
    main()