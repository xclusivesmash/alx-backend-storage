-- creates a stored procedure and stores
-- average scores for students.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INTEGER)
BEGIN
    DECLARE scores INTEGER DEFAULT 0;
    DECLARE projects_ INTEGER DEFAULT 0;
    SELECT SUM(score) INTO scores FROM corrections WHERE corrections.user_id = user_id;
    SELECT COUNT(*) INTO projects_ FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET users.average_score = IF(projects_ = 0, 0, scores / projects_) WHERE users.id = user_id;
END $$
DELIMITER ;
