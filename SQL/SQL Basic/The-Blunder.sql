select CEIL(avg(salary) - avg(replace(salary, '0', '')))
from EMPLOYEES 