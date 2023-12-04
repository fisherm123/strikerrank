create table shots as
with player_id as(
	select distinct players.id as id, fbref.name as name
	from players left join tfmkt on
	(players.first = tfmkt.first or players.first is NULL and tfmkt.first is NULL) and
	(players.last = tfmkt.last or players.last is NULL and tfmkt.last is NULL) and
	(players.height = tfmkt.height or players.height is NULL and tfmkt.height is NULL) and
	(players.val = tfmkt.val or players.val is NULL and tfmkt.val is NULL) and
	(players.img = tfmkt.img or players.img is NULL and tfmkt.img is NULL)
	left join fbref on tfmkt.join = fbref.join_column
)


select 
	matches.id as game_id, minute, players1.id as player_id, teams.id as team_id, "xG", 
	"PSxG", goal, distance, body_part, players2.id as ast1_id, players3.id as ast2_id
from shots_raw
left join matches on matches.join = shots_raw.game
left join player_id as players1 on players1.name = shots_raw.player
left join player_id as players2 on players2.name = shots_raw.assister1
left join player_id as players3 on players3.name = shots_raw.assister2
left join teams on teams.name = shots_raw.team

