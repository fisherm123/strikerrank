# soccerdatabase

**Introduction:**

The goal of this project is to conduct on analysis of player statistics from the 2022-23 soccer season from the top 5 leagues in Europe (as well as major international competitions those players were part of) contrasted with current estimated market values of those players. We will accomplish this by gathering data from the 2022-23 season from relevant leagues, put together a database of key information from this data, and develop a user interface through a web app that will allow users to see the results of our analysis as well as develop their own insights.

**Scope of Data:**

The data included in this project will be from the 2022-23 seasons of the English Premier League, Spanish La Liga, French Ligue 1, Italian Serie A, and German Bundesliga, FIFA World Cup, and UEFA Champions League. Game statistics are gathered from [fbref.com](https://fbref.com/en/comps/). Player statistics including market value are gathered from https://www.transfermarkt.co.uk/.

**Project Architecture:**

The project has 3 major working components: the web scrapers (found in scraper directory), the database (found in database directory), and the web app (found in web_app directory). 

The web scrapers have been adapted from scrapers used in projects linked HERE and HERE. They were several years out of date, and had to be fixed to reflect the new layout of the source sites, but largely had a working foundation to crawl the web pages that didn't require alterations. Our adapted versions including information on our changes are included in the scraper directory.

