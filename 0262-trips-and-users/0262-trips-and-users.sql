WITH first_table AS (
    SELECT 
        t.request_at AS Day,
        COUNT(*) AS cnt
    FROM Trips t
    JOIN Users u1 ON t.client_id = u1.users_id
    JOIN Users u2 ON t.driver_id = u2.users_id
    WHERE u1.banned = 'No'
      AND u2.banned = 'No'
    GROUP BY t.request_at
),

second_table AS (
    SELECT 
        t.request_at AS Day,
        COUNT(*) AS cancelled_cnt
    FROM Trips t
    JOIN Users u1 ON t.client_id = u1.users_id
    JOIN Users u2 ON t.driver_id = u2.users_id
    WHERE u1.banned = 'No'
      AND u2.banned = 'No'
      AND t.status IN ('cancelled_by_client', 'cancelled_by_driver')
    GROUP BY t.request_at
)

SELECT 
    t1.Day,
    ROUND(
        COALESCE(t2.cancelled_cnt, 0) / t1.cnt,
        2
    ) AS `Cancellation Rate`
FROM first_table t1
LEFT JOIN second_table t2
    ON t1.Day = t2.Day
WHERE t1.Day BETWEEN '2013-10-01' AND '2013-10-03';