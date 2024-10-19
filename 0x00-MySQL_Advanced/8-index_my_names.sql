--  script that creates an index idx_name_first on the table names and the first letter of name

ALTER TABLE names
ADD first_letter CHAR(1);

DELIMITER //
DROP TRIGGER IF EXISTS before_insert_names;
CREATE TRIGGER before_insert_names
BEFORE INSERT ON  names
FOR EACH ROW
BEGIN
	SET NEW.first_letter = LEFT(NEW.name, 1);
END; //
DELIMITER ;



DELIMITER //
DROP TRIGGER IF EXISTS after_update_names;
CREATE TRIGGER after_update_names
BEFORE UPDATE ON names
FOR EACH ROW
BEGIN
	SET NEW.first_letter = LEFT(NEW.name, 1);
END; //
DELIMITER ;
