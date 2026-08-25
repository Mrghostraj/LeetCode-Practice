# Write your MySQL query statement below
SELECT 
    ROUND(SUM(CASE WHEN first_order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)* 100 / COUNT(first_order_date) , 2) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) as first_order_date
    FROM Delivery 
    GROUP BY customer_id
) t
ON d.customer_id = t.customer_id
AND d.order_date = t.first_order_date;