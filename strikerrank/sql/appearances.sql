create table appearances as
with player_id_table as(
	select distinct players.id as id, fbref.name as name
	from players left join tfmkt on
	(players.first = tfmkt.first or players.first is NULL and tfmkt.first is NULL) and
	(players.last = tfmkt.last or players.last is NULL and tfmkt.last is NULL) and
	(players.height = tfmkt.height or players.height is NULL and tfmkt.height is NULL) and
	(players.val = tfmkt.val or players.val is NULL and tfmkt.val is NULL) and
	(players.img = tfmkt.img or players.img is NULL and tfmkt.img is NULL)
	left join fbref on tfmkt.join = fbref.join_column
)

select matches.id as match_id, teams.id as team_id ,player_id_table.id as player_id, minutes, "GIs", "Ast", "PK", "PKatt", "Yellow", "Red", "xG", "npxG", "xAG"
from appearances_raw left join 
matches on appearances_raw.game = matches.join
left join player_id_table on player_id_table.name = appearances_raw.player
left join teams on appearances_raw.team = teams.name
order by match_id


