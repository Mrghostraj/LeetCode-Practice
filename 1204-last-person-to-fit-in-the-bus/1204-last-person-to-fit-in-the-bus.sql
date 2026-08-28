# Write your MySQL query statement below
SELECT t.person_name
FROM (
    SELECT * ,
    SUM(weight) OVER (ORDER BY turn) AS total_weight
FROM Queue
) t
WHERE t.total_weight <=1000
ORDER by t.turn DESC
LIMIT 1;