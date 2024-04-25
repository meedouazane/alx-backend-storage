-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SELECT users.id, users.name, CAST(AVG(corrections.score) AS DECIMAL(10,0)) AS average_score 
    FROM corrections 
    INNER JOIN users ON user_id = users.id 
    WHERE users.id=user_id
    GROUP BY users.id, users.name;
END
