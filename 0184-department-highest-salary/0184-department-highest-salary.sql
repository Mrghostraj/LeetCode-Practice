# Write your MySQL query statement below
with join_table as (
    select d.name as Department, 
    e.name as Employee, 
    e.salary,
    dense_rank() over (
        partition by d.name
        order by e.salary desc
    ) as rnk 
from Employee e
JOIN Department d
on e.departmentId = d.id
)
select Department, Employee, salary 
from join_table 
where rnk = 1;
 