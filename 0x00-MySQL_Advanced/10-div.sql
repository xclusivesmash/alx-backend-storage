-- creates a function SafeDiv that divides (and returns) the
-- first by the second number or returns 0 if the second number is equal to 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INTEGER, b INTEGER)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE outcome FLOAT DEFAULT 0;
    IF b != 0 THEN
        SET outcome = a / b;
    END IF;
    RETURN outcome;
END $$
DELIMITER ;
