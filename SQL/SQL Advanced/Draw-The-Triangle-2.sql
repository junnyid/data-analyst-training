select repeat ('* ', n)
from (
    select @row := @row + 1 AS n
    from information_schema.tables, (select @row := 0) r
    limit 20
) as numbers;

/* if you want to understand for the detail

select repeat ('* ', n)
from (
select 1 as n union all
select 2 union all
select 3 union all
select 4 union all
select 5 union all
select 6 union all
select 7 union all
select 8 union all
select 9 union all
select 10 union all
select 11 union all
select 12 union all
select 13 union all
select 14 union all
select 15 union all
select 16 union all
select 17 union all
select 18 union all
select 19 union all
select 20 ) as numbers

 */