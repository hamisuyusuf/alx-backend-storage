-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Declare a variable to hold the result
    DECLARE result FLOAT;

    -- Check if the denominator is zero
    IF b = 0 THEN
        -- Return 0 if the denominator is zero
        SET result = 0;
    ELSE
        -- Perform the division if the denominator is not zero
        SET result = a / b;
    END IF;

    -- Return the result
    RETURN result;
END //

DELIMITER ;

