select COUNTRY.Continent, floor(avg(CITY.Population)) from CITY
join COUNTRY on  CITY.CountryCode = COUNTRY.Code
group by COUNTRY.Continent