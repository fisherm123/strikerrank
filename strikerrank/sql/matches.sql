create table matches as
(
	select _matches_raw.id, team1.id as home_id, team2.id as away_id, date, neutral
	from _matches_raw left join teams as team1 on home = team1.name
	left join teams as team2 on away = team2.name
)
