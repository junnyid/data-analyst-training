select CONCAT(Name, '(', SUBSTR(Occupation, 1, 1), ')')
from OCCUPATIONS
order by Name;

select concat('There are a total of ', COUNT(*), ' ',  lower(occupation), "s.")
from OCCUPATIONS 
Group by Occupation 
Order by COUNT(*), Occupation
