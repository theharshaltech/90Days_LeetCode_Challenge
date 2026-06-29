# Write your MySQL query statement below
-- SELECT customer_id , COUNT(*) FROM Visits LEFT JOIN Transactios ON Visit.visit_id = Transaction.visit_id WHERE Transaction.visit_id IS NULL GROUP BY customer_id

SELECT customer_id, COUNT(*) AS count_no_trans FROM Visits LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id WHERE Transactions.visit_id IS NULL GROUP BY customer_id;