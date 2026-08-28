# Write your MySQL query statement below
SELECT t.person_name
FROM (
    SELECT * ,
    SUM(weight) OVER (ORDER BY turn) AS total_weight
FROM Queue
ORDER BY turn
) t
WHERE t.total_weight <=1000
ORDER by t.total_weight DESC
LIMIT 1;