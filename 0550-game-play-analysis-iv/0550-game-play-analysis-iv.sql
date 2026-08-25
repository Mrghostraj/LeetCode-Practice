# Write your MySQL query statement below
SELECT 
    ROUND(SUM(CASE WHEN DATE_ADD(t.first_date, INTERVAL 1 day) = a.event_date THEN 1 ELSE 0 END)/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM Activity a 
JOIN 
     (SELECT player_id, MIN(event_date) AS first_date
    FROM Activity 
    GROUP BY player_id) t
ON a.player_id = t.player_id;