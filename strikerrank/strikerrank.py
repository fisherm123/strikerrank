import psycopg2
from psycopg2 import sql
from flask import Flask, render_template, request

app = Flask(__name__)


con = psycopg2.connect(database="worldsoccer", host="localhost", user="postgres", 
                       password="musowls14", port="5432")

cursor = con.cursor()

@app.route('/strikerrank', methods=["GET"])
def striker():

    n = request.args.get('n')
    if n == None:
        n = 10
    else:
        n = int(n)
        
    initial_table = """with shot_summary as (

    select players.id, img, first, last, sum(shots.xg) as sum_xg, sum(goal) as rg, val, dob
    from players
    left join shots on shots.player_id = players.id
    group by players.id, img, first, last, val, dob
    having sum(shots.xg) > 0
    order by sum(shots.xg) desc)

    select img, first, last, max(sum_xg) as my_xg, rg, val, id
    from shot_summary
    left join appearances on id = player_id
    where dob > '11-24-1993'
    group by img, first, last, rg, val, id
    having sum(minutes) > 1000
    order by (rg - max(sum_xg)) desc"""

    cursor.execute(initial_table)
    table = cursor.fetchmany(n)

    leagues_q = "select name from leagues where type = 0"
    
    cursor.execute(leagues_q)
    leagues = cursor.fetchall()

    return render_template('strikerrank.html', data=table, league_options=leagues, selected = 'all')

@app.route('/update/<sel_league>', methods=["GET", "POST"])
def update(sel_league):

    n = request.args.get('n')
    if n == None:
        n = 10
    else:
        n = int(n)

    d = {"Bundesliga":0, "La Liga":2, "Ligue 1":3, "Premier League": 4, "Serie A": 5}
        
    initial_table = sql.SQL(
            """with included_appearances as (

            select * from teams
            left join appearances on id = team_id
            where league = {}),
            
            shot_summary as (

            select players.id, img, first, last, sum(shots.xg) as sum_xg, sum(goal) as rg, val, dob
            from players
            left join shots on shots.player_id = players.id
            group by players.id, img, first, last, val, dob
            having sum(shots.xg) > 0
            order by sum(shots.xg) desc)

            select img, first, last, max(sum_xg) as my_xg, rg, val, shot_summary.id
            from shot_summary
            right join included_appearances on shot_summary.id = player_id
            where dob > '11-24-1993'
            group by shot_summary.id, img, first, last, rg, val, shot_summary.id
            having sum(minutes) > 1000
            order by (rg - max(sum_xg)) desc""").format(sql.Literal(d[sel_league]))

    leagues_q = "select name from leagues where type = 0"
    
    cursor.execute(leagues_q)
    leagues = cursor.fetchall()

    cursor.execute(initial_table)
    table = cursor.fetchmany(n)

    return render_template('strikerrank.html', data=table, league_options = leagues, selected = sel_league)

@app.route('/player/<id>', methods=["GET"])
def player(id):

    player_q = """select * from players where id = {}""".format(id)

    appearances_q = """select home.name, away.name, played_for.name, matches.date, minutes, gi, ast, pk, pk_att, yellow, red, xg, npxg, xag
    from appearances 
    left join teams as played_for on played_for.id = team_id
    left join matches on match_id = matches.id
    left join teams as home on matches.home_id = home.id
    left join teams as away on matches.away_id = away.id
    where player_id = {}
    order by matches.date asc""".format(id)

    cursor.execute(appearances_q)
    table = cursor.fetchall()

    cursor.execute(player_q)
    player_info = cursor.fetchone()
    return render_template('player.html', player_info = player_info, table = table)
