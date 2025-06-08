/* Samantha interviews many candidates from different colleges using coding challenges and contests.
Write a query to print the contest_id, hacker_id, name, 
and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. 
Exclude the contest from the result if all four sums are 0. */

SELECT c.contest_id, c.hacker_id, c.name, 
coalesce(sum(ts), 0), coalesce(sum(tas), 0), coalesce(sum(tv), 0), coalesce(sum(tuv), 0)

from Contests as c
join Colleges as cl on c.contest_id = cl.contest_id
join Challenges as ch on ch.college_id = cl.college_id
LEFT JOIN (
    SELECT challenge_id, 
    sum(total_views) as tv,
    sum(total_unique_views) as tuv
    FROM View_Stats
    GROUP BY challenge_id
) as vs on ch.challenge_id = vs.challenge_id
LEFT JOIN (
    SELECT challenge_id, 
    sum(total_submissions) as ts, 
    sum(total_accepted_submissions) as tas
    FROM Submission_Stats
    GROUP BY challenge_id
) as ss on ch.challenge_id = ss.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING
    coalesce(sum(ts), 0) > 0 or 
    coalesce(sum(tas), 0) > 0 or
    coalesce(sum(tv), 0) > 0 or 
    coalesce(sum(tuv), 0) > 0 
ORDER BY c.contest_id