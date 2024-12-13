-- creates a stored procedure that adds a correction
-- for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INTEGER, project_name VARCHAR(255), score FLOAT)
BEGIN
    DECLARE project_ INT DEFAULT 0;
    DECLARE project_id INT DEFAULT 0;
    SELECT COUNT(id) INTO project_ FROM projects WHERE name = project_name;
    IF project_ = 0 THEN
        INSERT INTO projects(name)
            VALUES(project_name);
    END IF;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;
