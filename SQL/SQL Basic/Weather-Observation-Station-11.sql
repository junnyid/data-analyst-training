SELECT DISTINCT CITY
FROM STATION
WHERE NOT (UPPER(SUBSTRING(CITY, 1, 1)) IN ('A', 'E', 'I', 'O', 'U') 
           AND UPPER(SUBSTRING(CITY, LENGTH(CITY), 1)) IN ('A', 'E', 'I', 'O', 'U'));
