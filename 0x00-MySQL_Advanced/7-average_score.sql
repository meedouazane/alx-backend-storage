-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT CAST(AVG(corrections.score) AS DECIMAL(10,0)) FROM corrections WHERE corrections.user_id = id)
    WHERE users.id = user_id;
END //
DELIMITER;
