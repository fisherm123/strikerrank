# Data

**Data Sources**

Files with the tfmkt prefix came from information scraped off of the TransferMarkt website through a web scraper we forked here: 
https://github.com/fisherm123/transfermarkt-scraper. All other data was scraped off of FBRef through a web scraper we forked here:
https://github.com/fisherm123/soccerdata.

**Cleaning Process**

Our data was cleaned in several ways. 

Firstly, the unique identifiers that we pulled from each match in our resulting dataset was
a string consisting of the two teams playing in the match with the date of the match. The plan was to later match each of these
unique strings with an integer id to use as a primary key for the match. However, after putting the resulting match.csv file
in excel and running a uniqueness check, we discovered that for matches without a Home/Away team (where the match was set
at a neutral venue) the match string only contained the name of the lexigraphically smaller team name, which caused some matches
to have the same identification string. As such, we had to fix these issues by constructing our own identifier for the match
off of the other fields for the tuple so that we could later assign a unique integer for it (some of the matches were scraped
more than once so we couldn't do this immediately, we first needed this string so we could tell which ones were duplicates).

Secondly, we cleaned the data by standardizing the alphabet for names. Each of our two datasets used different alphabets for the
names of players (for example one used Russian letters for players who go by their Russian name and one used an English transliteration
of the Russian name). So, in excel we used a conversion function to make sure that all names are only using the same set of letters.

Thirdly, the two sites sometimes different names for a given team. For example, one site used "Newcastle" while the other used
"Newcastle United". We again tried resolving this through a fuzzy match, but this introduced too many obvious errors for cases like
"Man Utd" and "Manchester United" getting mixed up with "Man City".

**Entity Resolution**

Resolving our two datasets (player information from RBRef and player information from TransferMarkt) was one of the biggest 
challenges of this project. 

Soccer players often go by nicknames, come from contries with different naming conventions (such
as putting family name first), and many other differences. As such, matching names across these two datasets wasn't as simple
as performing a join on the names. For many, such as most of the English Premier League players, both sites agreed on the name.
But often, there wasn't an exact match. We tried using different fuzzy join algorithms to varying degrees of success (before
we cleaned the names to use the same alphabet), but this still left several hundred errors when one site was using nicknames
completely unrelated to the player's actual name. After standardizing our alphabets, we were able to do a simple join that
left only a couple hundred gaps. In the end, we had to simply resolve this manually by querying for unmatched tuples,
and trying to find a match in the other table by eye, and if that didn't work simply by looking up the player's name in the other
site.

We also had difficulty resolving player entities as a result of transfers across teams. The scrapers got player info by scraping
information off of team rosters. So, for players that played for multiple teams, their info would be scraped twice. This wasn't
easily solvable by removing duplicate names, as duplicate names sometimes corresponded to different entities. We resolved this by
selecting entities uniquely on both name and birthday.
