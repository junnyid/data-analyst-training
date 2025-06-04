Select MAX(salary * months), COUNT(*)
FROM Employee 
Where salary * months = (SELECT MAX(salary * months) FROM Employee)