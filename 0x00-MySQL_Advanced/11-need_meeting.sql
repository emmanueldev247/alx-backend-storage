--  script that creates a view need_meeting that lists all students
--  that have a score under 80 (strict) and no last_meeting or more than 1 month

DELIMITER //

CREATE VIEW need_meeting AS
SELECT name
FROM students; //

DELIMITER ;
