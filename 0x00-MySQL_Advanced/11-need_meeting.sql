-- script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
CREATE view need_meeting as
SELECT name 
FROM students 
WHERE score < 80 
AND (TIMESTAMPDIFF(MONTH, last_meeting, NOW()) > 1 OR last_meeting IS NULL);
