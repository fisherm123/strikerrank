import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


con = psycopg2.connect(database="worldsoccer", host="localhost", user="postgres", 
                       password="musowls14", port="5432")

cursor = con.cursor()

@app.route('/strikerrank')
def striker():

    initial_table = """with shot_summary as (

	select players.id, img, first, last, sum(shots.xg) as sum_xg, sum(goal) as rg, val, dob
	from players
	left join shots on shots.player_id = players.id
	group by players.id, img, first, last, val, dob
	having sum(shots.xg) > 0
	order by sum(shots.xg) desc)

    select img, first, last, max(sum_xg) as my_xg, rg, val
    from shot_summary
    left join appearances on id = player_id
    where dob > '11-24-1993'
    group by img, first, last, rg, val
    having sum(minutes) > 1000
    order by (rg - max(sum_xg)) desc"""

    cursor.execute(initial_table)
    table = cursor.fetchmany(10)

    leagues_q = "select league from leagues order by international asc"
    cursor.execute(leagues_q)
    leagues = cursor.fetchall()

    teams_q = "select name from teams"
    cursor.execute(teams_q)
    teams = cursor.fetchall()

    return render_template('strikerrank.html', data=table, league_options=leagues, team_options=teams)
    