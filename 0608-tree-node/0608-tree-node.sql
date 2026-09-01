# Write your MySQL query statement below
select t1.id, 
    (case   when t1.p_id is null then 'Root'
            when t2.id is not null then 'Inner'
            else 'Leaf'
    end) as type
from Tree t1
left JOIN Tree t2
on t1.id = t2.p_id
group by t1.id;