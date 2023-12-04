create table players_raw as
select 
	id, first, last, birth::date as dob, height, cit, pos, img, nat_team, foot, val 
from fbref left join tfmkt
on fbref.join_column = tfmkt.join

