/*You are given a table, Functions, containing two columns: X and Y.
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.*/

SELECT Distinct A.X, A.Y
FROM Functions AS A
JOIN Functions AS B
ON A.X = B.Y
AND B.X = A.Y
where A.X < A.Y

union

SELECT Distinct X, Y
FROM Functions 
where X = Y
group by X, Y
having count(*) > 1

order by X