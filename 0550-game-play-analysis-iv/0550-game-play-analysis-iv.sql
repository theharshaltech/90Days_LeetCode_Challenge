# Write your MySQL query statement below
select ROUND( COUNT(*) / (select COUNT(distinct player_id) from Activity), 2 ) as fraction
from Activity a JOIN ( select player_id, MIN(event_date) as first_login from Activity group by player_id ) f on a.player_id = f.player_id
and a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);