# Price Scraper 2 (v2)
New component price tracker, with a new approach and various fixes and upgrades. 

This is a small project of a price scraper for PC componentes sold in Amazon, PCC and Coolmod. 

The idea of the project is to have a tool that given a csv file with the links of the components in each store can scrap each one of those pages in order to get the component's price and get the cheapest build possible. 

As stated before, the scraper uses a csv file in order to read the information and BeautifulSoup for the parsing of each of the links.

There's a csv example file in the project for the components. This file should be placed in the root folder of the project or wherever you feel like after changing the CSV_FILE variable in constants.py. 

This new v2 version is also compatible to be used as a part of a Telegram bot (with AWS Lambda or any other service/system you'd like to use). 
Just set the CHAT_ID and the TOKEN as environment variables for your bot, and you should be good to go.
