/* Julia conducted a 15 days of learning SQL contest.
 The start date of the contest was March 01, 2016 and the end date was March 15, 2016. 
 Write a query to print total number of unique hackers who made at least 1 submission each day 
 (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. 
 If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. 
 The query should print this information for each day of the contest, sorted by the date.*/
SELECT submission_date,
    (
        SELECT COUNT(DISTINCT hacker_id)
        FROM Submissions AS s2
        WHERE s2.submission_date = s1.submission_date
            AND DATEDIFF(s1.submission_date, '2016-03-01') = (
                SELECT COUNT(DISTINCT submission_date)
                FROM Submissions AS s3
                WHERE s3.hacker_id = s2.hacker_id
                    AND s3.submission_date < s2.submission_date
            )
    ),
    (
        SELECT hacker_id
        FROM Submissions AS s4
        WHERE s4.submission_date = s1.submission_date
        GROUP BY hacker_id
        ORDER BY COUNT(submission_id) DESC,
            hacker_id ASC
        LIMIT 1
    ) AS id,
    (
        SELECT name
        FROM Hackers
        WHERE hacker_id = id
    )
FROM (
        SELECT DISTINCT submission_date
        FROM Submissions
        where submission_date BETWEEN '2016-03-01' and '2016-03-15'
    ) AS s1;