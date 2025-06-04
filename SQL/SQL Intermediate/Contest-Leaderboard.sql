select h.hacker_id, h.name, sum(max_scores.max_score) as total
from Hackers as h
join (select s.hacker_id, s.challenge_id, MAX(s.score) as max_score from Submissions as s group by s.hacker_id, s.challenge_id) as max_scores on h.hacker_id = max_scores.hacker_id
group by h.hacker_id, h.name
having sum(max_scores.max_score) > 0
order by total desc, h.hacker_id