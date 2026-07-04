# Write your MySQL query statement below
SELECT visited_on, SUM(amount) OVER ( ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ) AS amount, ROUND( AVG(amount) OVER ( ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ), 2 ) AS average_amount
FROM ( SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY visited_on
) t LIMIT 1000000 OFFSET 6;