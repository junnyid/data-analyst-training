SELECT SUBMISSIONS.hacker_id, name
FROM SUBMISSIONS
JOIN HACKERS ON SUBMISSIONS.hacker_id = HACKERS.hacker_id
JOIN Challenges ON SUBMISSIONS.challenge_id = Challenges.challenge_id
JOIN Difficulty ON Challenges.difficulty_level = Difficulty.difficulty_level
WHERE SUBMISSIONS.score = Difficulty.score
GROUP BY name, SUBMISSIONS.hacker_id
HAVING count(SUBMISSIONS.challenge_id) > 1
ORDER BY count(SUBMISSIONS.challenge_id) DESC, SUBMISSIONS.hacker_id