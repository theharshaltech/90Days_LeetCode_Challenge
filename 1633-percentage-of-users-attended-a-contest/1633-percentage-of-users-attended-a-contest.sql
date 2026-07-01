# Write your MySQL query statement below
SELECT contest_id , Round(count(user_id) * 100.0 / (select count(*) from Users), 2) as percentage from 
Register group by contest_id order by percentage desc , contest_id asc;