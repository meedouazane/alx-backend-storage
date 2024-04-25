-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
	SELECT AVG(corrections.score) 
	FROM corrections 
	WHERE corrections.user_id = users.id)
    WHERE users.id = user_id;
END //
DELIMITER;
