# Write your MySQL query statement below
#SELECT id FROM Weather SELF JOIN Weather ON Weather.recoderDate = Weater.recoderDate WHERE Weather.temperature IS GROUP BY id;

SELECT w1.id FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 WHERE w1.temperature > w2.temperature;