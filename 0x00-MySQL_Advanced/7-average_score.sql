--  script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(
		IN user_id INT
)
BEGIN
	DECLARE average_score FLOAT;

	SELECT AVG(score) INTO average_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	IF average_score IS NOT NULL THEN
		UPDATE users
		SET users.average_score = average_score
		WHERE users.id = user_id;
	END IF;
END; //


DELIMITER ;
