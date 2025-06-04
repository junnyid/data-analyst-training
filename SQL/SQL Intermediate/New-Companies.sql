select C.company_code, C.founder, COUNT(distinct LM.lead_manager_code), COUNT(distinct SM.senior_manager_code), COUNT(distinct M.manager_code), COUNT(distinct E.employee_code)
from Company C
JOIN Lead_Manager LM ON C.company_code = LM.company_code
JOIN Senior_Manager SM ON LM.lead_manager_code = SM.lead_manager_code
JOIN Manager M ON SM.senior_manager_code = M.senior_manager_code
JOIN Employee E ON M.manager_code = E.manager_code
Group by C.company_code, C.founder
Order by C.company_code