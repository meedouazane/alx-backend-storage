-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER //
CREATE TRIGGER email_changes
AFTER UPDATE ON users
FOR EACH ROW
IF NEW.email <> OLD.email THEN
UPDATE users
SET valid_email = 0
WHERE id = NEW.id;
END IF;
//
DELIMITER ;
