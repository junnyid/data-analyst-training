select c.hacker_id, h.name, count(c.challenge_id) as total
from Hackers as h
join Challenges as c on h.hacker_id = c.hacker_id
group by c.hacker_id, h.name
having total = (select count(c1.challenge_id) from Challenges as c1 group by c1.hacker_id order by count(*) desc limit 1)
or total not in (select count(c2.challenge_id) from Challenges as c2 group by c2.hacker_id having c2.hacker_id <> c.hacker_id)
order by total desc, c.hacker_id;