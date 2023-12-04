# Database Code

**Postgresql Server:**

Our database was managed through a Postgresql server which we connect to through the psycopg2 library. A dump of the database is included in the srdb.sql file.

**Database Layout:**

Our database consists of two tiers of tables. The lower tier, denoted by tables whose name is preceded by an underscore, consists of tables into which the cleaned .csv files have been imported. These tables are then queried to create the higher tier of tables whose name does not begin with an underscore. The queries used to create each higher tier table is included in a sql file in this directory of a corresponding name.




