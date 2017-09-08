# price_scraper2
New component price tracker, with a new approach and various fixes and upgrades. 

This is a small project of a price scraper for PC componentes sold in Amazon, PCC and Coolmod. 

The idea of the project is to have a tool that given a small JSON file with just a bit of info about the components in each store can scrap each one of those pages in order to get the component's price and get the cheapest build possible. 

As stated before, the scraper uses a JSON file in order to read and store the information as well as lxml and custom XPATH for each store in order to get the required information for the scraper to do its job.

There's a JSON template in the project for the components list file, file that should be placed in the root root folder of the project. File route can be changed in the configuration file. 

<br>
The required IDs for every store are: 

<b> Amazon </b>
  - The string of numbers and letters that appears on every product url -- similar to "B073BVHY3F"

<b> PCC </b>
  - Everything that appears after .com/ in the product url
  
<b> Coolmod </b>
  - Everything that appears after .com/ in the product url
