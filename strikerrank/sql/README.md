# Database Code

**Postgresql Server:**

Our database was managed and created through the pgAdmin tool and hosted on a postgres server which our web app connects to using the psycopg2 Python library. A dump of the database created in pgAdmin is included in the **srdb.sql** file.

**Database Layout:**

Our database consists of two tiers of tables. The lower tier, denoted by tables whose name is preceded by an underscore, consists of tables into which the cleaned .csv files have been imported. These tables are then queried to create the higher tier of tables whose name does not begin with an underscore. The queries used to create each higher tier table is included in a sql file in this directory of a corresponding name. This sets us up nicely for expanding the scope of the project. To add new leagues or season data, we simply need to rerun the scraper and import the data into our raw tables.

We experimented with using views and materialized views for the tables in blue, but views were too slow from a performance perspective with
our web app, and both views and materialized views don't allow imposing additional constraints on the data that we wanted after data
transformations, so we chose to implement these as their own tables. Leaving the raw tables facilitates the process of adding more raw
imported data in the future for our web app.

![alt text](https://github.com/fisherm123/strikerrank/blob/main/strikerrank/sql/database_design.png)

**Schema:**

![alt text](https://github.com/fisherm123/strikerrank/blob/main/strikerrank/sql/schema.png)

Major Design Choices:
* We didn't include match score as an attribute of the matches since we are performing player-based analysis and don't actually
  care who won the game. All we care about is individual players' goals, not which team ended up with the points as a result.
* We didn't include any team attributes for players (besides national team which is not transferable) since players can transfer
  between various teams throughout the season. This information can instead be derived from the appearances table, which expresses
  matches that a player has played for a given team.
* Player images are saved as a url for the image instead of the image itself. This is again to save space, and we were able to accomplish
  this since our scraper can very easily just take the url for an image instead of the image itself. The web app can instead be responsible
  for rendering the image if/when needed.
  
