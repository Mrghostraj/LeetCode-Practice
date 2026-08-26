SELECT all_p.product_id,
       COALESCE(p.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) all_p
LEFT JOIN (
    SELECT p1.product_id, p1.new_price
    FROM Products p1
    JOIN (
        SELECT product_id, MAX(change_date) AS latest_date
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    ) t
    ON p1.product_id = t.product_id
    AND p1.change_date = t.latest_date
) p
ON all_p.product_id = p.product_id;