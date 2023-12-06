import psycopg2
from psycopg2 import sql
from flask import Flask, render_template, request

app = Flask(__name__)


con = psycopg2.connect(database="worldsoccer", host="0.0.0.0", user="postgres", 
                       password="musowls14", port="5432")

cursor = con.cursor()

@app.route('/strikerrank', methods=["GET", "POST", "PUT"])
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

    select img, first, last, max(sum_xg) as my_xg, rg, val
    from shot_summary
    left join appearances on id = player_id
    where dob > '11-24-1993'
    group by img, first, last, rg, val
    having sum(minutes) > 1000
    order by (rg - max(sum_xg)) desc"""

    cursor.execute(initial_table)
    table = cursor.fetchmany(n)

    leagues_q = "select league from leagues where international = 'domestic' order by international asc"
    cursor.execute(leagues_q)
    leagues = cursor.fetchall()

    return render_template('strikerrank.html', data=table, league_options=leagues, selected = 'all', num = n)

@app.route('/update/<league>', methods=["POST", "GET"])
def update(league):

    n = request.args.get('n')
    if n == None:
        n = 10
    else:
        n = int(n)
        
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

            select img, first, last, max(sum_xg) as my_xg, rg, val
            from shot_summary
            right join included_appearances on shot_summary.id = player_id
            where dob > '11-24-1993'
            group by shot_summary.id, img, first, last, rg, val
            having sum(minutes) > 1000
            order by (rg - max(sum_xg)) desc""").format(sql.Literal(league))

    leagues_q = "select league from leagues where international = 'domestic' order by international asc"
    cursor.execute(leagues_q)
    leagues = cursor.fetchall()

    cursor.execute(initial_table)
    table = cursor.fetchmany(n)
    return render_template('strikerrank.html', data=table, league_options = leagues, selected = league, num = n)
