# Database Code

**Postgresql Server:**

Our database was managed and created through the pgAdmin tool and hosted on a postgres server which our web app connects to using the psycopg2 Python library. A dump of the database created in pgAdmin is included in the srdb.sql file.

**Database Layout:**

Our database consists of two tiers of tables. The lower tier, denoted by tables whose name is preceded by an underscore, consists of tables into which the cleaned .csv files have been imported. These tables are then queried to create the higher tier of tables whose name does not begin with an underscore. The queries used to create each higher tier table is included in a sql file in this directory of a corresponding name.

![alt text](https://github.com/fisherm123/strikerrank/blob/main/strikerrank/sql/database_design.png)

**Schema:**

https://github.com/fisherm123/strikerrank/blob/main/strikerrank/sql/schema.png


