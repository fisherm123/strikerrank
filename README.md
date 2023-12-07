# StrikerRank

**Note**

The repository contains additional README files in subdirectories to give an explanation of the work done for each of the rubric items.

**Introduction and Goals:**

There are many different existing websites that provide soccer statistics. However, the most extensive, reliable, and popular sources tend to specialize in certain areas. FBRef provides an enourmous volume of raw data, but can be too difficult to sort through and doesn't update player market values frequently. TransferMarkt specializes in primarily reporting accurate and up-to-date player market values, but doesn't have much else information. As such, we want to create a platform that combines the best of both worlds, giving the user a platform to compare game statistics with the current estimated value of a player.

The goal of this project is to conduct on analysis of player statistics from the 2022-23 soccer season from the top 5 leagues in Europe (as well as major international competitions those players were part of) contrasted with current estimated market values of those players. We will accomplish this by gathering data from the 2022-23 season from relevant leagues, put together a database of key information from this data, and develop a user interface through a web app that will allow users to see the results of our analysis as well as develop their own insights.

**Project Architecture:**

The project has 3 major working components: the web scrapers (links to forked projects below), the database (found in sql directory), and the web app. 

The web scrapers have been adapted from a TransferMarkt scraper I forked here: https://github.com/fisherm123/transfermarkt-scraper and a FBRef scraper I forked here: https://github.com/fisherm123/soccerdata/tree/master. They were several years out of date, and had to be fixed to reflect the new layout of the source sites, but largely had a working foundation to crawl the web pages that didn't require alterations. Scripts used to execute the scrapers are included alongside the output files in the scraper directory.

The database was developed and is hosted on a Postgresql server. The database schema documentation as well as SQL code for both tiers of the database is included in the database directory. A README for accessing the database server is included.

All code for the web app is included in the web_app directory. The web app uses the psycopg2 library to access the Postresql server, then a Flask render template is used to send query results to the web app that uses HTML, CSS, and JavaScript to present a UI for the main analysis of the project as well as tools to gather original insights. The focus is to show a ranking of the top strikers in the top 5 European leagues (described above) based on the key metrics we have chosen to highlight. The UI presents this information as well as filter options to narrow the scope of the data, as well as links to more in-depth information about specific players.

**Key Features:**

One key feature of the project is that as a result of our work fixing and updating the web scraping projects, the project can easily be expanded upon in following years by scraping data from other soccer leagues from around the world by just slightly altering the scraper execution script. The web app's filters are created dynamically upon start, so if you were to scrape data from the United States' Major League Soccer, you could incorporate it into the web app simply by importing the data into the database. No changes to the web app would need to be made to accomodate changes like this, as the filter options are created through a database query

The web app's features include:
  * a ranked list of players based on the key performance statistic described in our web app
  * the ability to filter the ranked list by competition
  * links to player-specific statistics page

**Our Data:**

The data included in this project will be from the 2022-23 seasons of the English Premier League, Spanish La Liga, French Ligue 1, Italian Serie A, and German Bundesliga, FIFA World Cup, and UEFA Champions League. Game statistics are gathered from [fbref.com](https://fbref.com/en/comps/). Player statistics including market value are gathered from https://www.transfermarkt.co.uk/.

From our scrapers, we collected information about the teams that currently play for the top 5 leagues in Europe, the players who play for these teams, matches from last leason, player appearances in these matches, as well as shots taken during these matches. The exact attributes we pulled from each of these categories is described in the csv README.

**Technical Challenges:**

The major techincal challenge of this project was collecting data, cleaning the data, and performing entity resolution on the player tuples. Despite European soccer having such worldwide popularity, we struggled to find a solid pre-existing dataset that would cover the needs of the project. As such, we decided to move into collecting our own data from sources that we knew to be both extensive and reliable so that we could handpick each and every statistic we were looking for.

This ended up being a much bigger task than originally anticipated, and ended up relying on repairing and augmenting existing web-scrapers rather than the development of our own from scratch. 

The difficulties didn't end here, as we were then faced with the task of coalescing our two separate data sources on the names of players written in various languages. One of the websites (TransferMarkt) tended to include the players' actual given names (which sometimes included accents and non-Latin letters), while the other (FBRef) tended not to. This meant that to connect the sources we had to first clean the names to get them as close as we could to each other (replacing accented letters with their English non-accented counterparts, ordering given and family names in English conventions, etc.), then performing a join and seeing the result. We were left with ~200 unmatched names (the matched names we performed spot tests and other constraint checks to validate correctness), which at the end of the day we had to resolve by hand. We experimented with different fuzzy-join algorithms, but the inaccuracies this often introduced (as soccer players tend to also go by very similar nicknames) led us to steer away from this. 
