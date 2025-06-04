select sum(c.POPULATION) from city as c 
join country as ct on c.CountryCode = ct.Code
where ct.CONTINENT = 'Asia'