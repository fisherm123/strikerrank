create table players as 
with dups as (
	select
		first, last, dob, height, cit, pos, img, nat_team, foot, val, row_number() over (partition by first, last, dob, height, cit, pos, img, nat_team, foot, val order by id) as row_num
	from players_raw
)

select 
	row_number() over (order by first, last, dob) as id, 
	first, last, dob, height, cit, pos, img, nat_team, foot, val
from dups
where row_num = 1