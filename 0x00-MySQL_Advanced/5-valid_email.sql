-- Task: Create a trigger to reset 'valid_email' to 0 when 'email' is changed in the 'users' table
-- This ensures that email validations are re-applied whenever a user's email address is updated

-- Change the delimiter to allow for trigger definition
DELIMITER //

-- Create the trigger
CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF (OLD.email <> NEW.email) THEN
        -- Reset 'valid_email' to 0 since the email has been updated
        SET NEW.valid_email = 0;
    END IF;
END;
//

-- Reset the delimiter to the default
DELIMITER ;

-- End of trigger creation script

