select 
case when G.Grade >= 8 then S.Name
else NULL
end as Names, G.Grade, S.Marks
from Students S
join Grades G on G.Max_Mark >= S.Marks and G.Min_Mark <= S.Marks
order by G.Grade desc, S.Name asc, S.Marks asc