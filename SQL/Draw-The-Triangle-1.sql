SELECT REPEAT('* ', 21 - n)
FROM (
    SELECT @row := @row + 1 AS n
    FROM information_schema.tables, (SELECT @row := 0) r
    LIMIT 20
) AS numbers;