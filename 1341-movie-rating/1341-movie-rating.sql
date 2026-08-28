# Write your MySQL query statement below
SELECT results
FROM(
    SELECT u.name AS results
    FROM MovieRating r
    JOIN Users u 
    ON r.user_id = u.user_id
    GROUP BY r.user_id, u.name
    ORDER BY COUNT(r.movie_id) DESC, u.name ASC
    LIMIT 1
) t1

UNION ALL

SELECT results
FROM (
    SELECT m.title AS results
    FROM MovieRating r
    JOIN Movies m
    ON r.movie_id =  m.movie_id
    WHERE r.created_at >= '2020-02-01'
        AND r.created_at < '2020-03-01'
    GROUP BY r.movie_id, m.title
    ORDER BY AVG(r.rating) DESC, m.title ASC
    LIMIT 1
) t2; 