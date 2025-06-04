Select distinct CITY
From STATION
Where lower(substr(CITY, 1, 1)) in ('a', 'e', 'i', 'o', 'u')
and lower(substr(CITY, -1, 1)) in ('a', 'e', 'i', 'o', 'u')