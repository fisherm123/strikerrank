#Web App

**Our Analysis**
For every shot a player takes, experts are able to determine a statistic known as "Expected Goal (xG)" for the shot. 
For a shot with xG of 0.5, this means that on average, this shot becomes a goal 50% of the time. One key metric for
determining the ability of a striker is to compare the amount of xG they accumulated during a game with their rG 
(actual goals). A good striker is able to score goals at a higher rate than the expected amount, so a good striker
should have a high value for xG - rG. 

Players also can be assigned a market value, determined by an estimate of about how much (in Euros for this project) a
team would have to pay in transfer fees to another team to buy that player for their team. 

Through this project, we are aiming to contrast this performance metric (xG - rG) with the market values of a player. As such,
on our main page we total up all of the xG and rG a player has accumulated for each shot, and rank them based on xG - rG. 
We also provide information about the player's market value, so the user can identify high value players. A player with
a high xG - rG with a low market value could possibly be a great transfer target for a team. For example, our third-
highest ranked player, Boulaye Dia, has nearly the same xG - rG as Erling Haaland, considered the best striker in the
Premier League. However, Boulaye Dia's market value can be seen on our home page to be ~9x lower than Erling Haaland's. This
suggests that Boulaye Dia might be a good transfer target for a team (someone they might want to look into acquiring), and is
the focus of our analysis.

**Features**

Our main page readily displays our top 10 players across all leagues, with the option to show additional rankings or filter
the results by a specific league. Additionally, each player comes with a link to a secondary page allowing the user
to get more detailed statistics and information about the player.

**Quick Start Guide**

To launch the web app, simply make sure that your environment has the required libraries, (psycopg2, Flask) and launch the web
app through the normal flask run process. Make sure the web app is exported to the flask app variable through:

> export FLASK_APP=strikerrank

Then run with:

> flask run
