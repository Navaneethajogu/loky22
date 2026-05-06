use college;
DROP PROCEDURE IF EXISTS lowest_marks;
delimiter &&
create procedure max_min()
begin
select min(marks)from lokesh;
select max(marks)from lokesh;
end &&
delimiter ;
call max_min();


use college;

DROP PROCEDURE IF EXISTS minmarks;
DELIMITER //

CREATE PROCEDURE minmarks()
BEGIN
    SELECT MIN(marks) AS min_marks FROM lokesh;
END //

DELIMITER ;
CALL minmarks();

DROP PROCEDURE IF EXISTS min_in_specific_sec;
use college;

select * from lokesh;
DROP PROCEDURE IF EXISTS min_in_specific_sec;
USE college;

DROP PROCEDURE IF EXISTS min_in_specific_sec;

CREATE PROCEDURE min_in_specific_sec(IN sec VARCHAR(50))
SELECT MIN(marks) 
FROM lokesh
WHERE section = sec;
CALL min_in_specific_sec('A');
CALL min_in_specific_sec('B');
CREATE PROCEDURE max_in_A_sec(OUT maximum INT)
SELECT MAX(marks) INTO maximum
FROM lokesh
WHERE section = 'A';
CALL max_in_A_sec(@l);
SELECT @l;

CREATE PROCEDURE max_in_sec(INOUT bonus INT)
SELECT MAX(marks) + bonus INTO bonus
FROM lokesh
WHERE section = 'A';
SET @b = 10;
CALL max_in_sec(@b);
SELECT @b;