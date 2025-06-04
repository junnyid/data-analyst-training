select CITY.name from CITY
join COUNTRY
on CITY.CountryCode = COUNTRY.Code
where COUNTRY.continent = 'Africa'