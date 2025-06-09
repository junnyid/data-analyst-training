/* Write a query to print all prime numbers less than or equal to 1000 . 
Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space). 
For example, the output for all prime numbers <= 10  would be: 2&3&5&7*/

WITH recursive numbers as (
    SELECT 2 as num
    union all
    SELECT num + 1 from numbers where num < 1000
),
divisors as (
    SELECT n.num, d.num as divisors
    from numbers n
    JOIN numbers d on d.num <= floor (sqrt(n.num)) and d.num < n.num
),
non_primes as(
    SELECT distinct num from divisors where mod(num, divisors) = 0
),
primes as (
    SELECT num from numbers
    where num not in (SELECT num from non_primes)
)
SELECT GROUP_CONCAT(primes.num ORDER BY primes.num SEPARATOR '&') AS prime_numbers
FROM primes;