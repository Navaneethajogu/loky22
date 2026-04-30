desc students;
select*from students;

 ### Select in table
select course from students;
select * from students where name="loky";
select * from students where age>10;
select*from students;
select * from students where age<13;
select*from students;
select * from students order by age;
select * from students order by age desc;





desc students;
select*from students;


select course from students;
select * from students where name="loky";
select * from students where age>10;
select*from students;
select * from students where age<13;
select*from students;
select * from students order by age;
select * from students order by age desc;

### Altering the table
select*from students;
alter table students add column  branch int;
alter table students modify column  branch int;
ALTER TABLE students
MODIFY COLUMN branch INT DEFAULT 1;
alter table students rename column  branch to performance;
alter table  students drop column performance;


SHOW TABLES;

DESC students;
select * from students;
insert into students values(1,"navaneetha",50),(2,"nava",70),(3,"neetha",80),(4,"nav",90);

SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1;
SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
SELECT COUNT(*) FROM students;
select * from students;
SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
select * from students;
SELECT DISTINCT marks 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
select * from students;


SHOW TABLES;

DESC students;
select * from students;
insert into students values(1,"navaneetha",50),(2,"nava",70),(3,"neetha",80),(4,"nav",90);

SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1;
SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
SELECT COUNT(*) FROM students;
select * from students;
SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
select * from students;
SELECT DISTINCT marks 
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
select * from students;

SELECT MAX(marks) FROM students;

SELECT * 
FROM students
WHERE marks = (SELECT MAX(marks) FROM students);
SELECT * FROM students WHERE marks = 90;
SELECT marks FROM students WHERE marks > 70;
SELECT * FROM students WHERE marks > 70;
SELECT marks FROM students WHERE marks > 70;
SELECT MAX(marks) 
FROM students
WHERE marks < (SELECT MAX(marks) FROM students);




use college;
create table stud(
roll_num int primary key,
name varchar(50),
email varchar(100)
);

insert into stud values
(121,"A","a@email.com"),
(122,"B","b@email.com"),
(123,"C","c@email.com")
select * from course
create table course(
course_id int primary key,
name varchar(50)
);

insert into course values
(1,"python"),
(2,"java"),
(3,"C++")
select * from course
use college;
select * from stud;
select * from course;
desc stud;
select * from stud;
select * from course;
insert into association values
(122,1),
(121,3),
(122,1);
select * from association;
use college;
select * from stud;
select * from course;
desc stud;
select * from stud;
select * from course;
insert into association values
(122,1),
(121,3),
(122,1);
select * from association;
## join tables ###
select * from stud join association as a on stud.roll_num=a.stud_id;

### types of joins #####
SELECT stud.roll_num, stud.name, stud.email, association.course_id
FROM stud
INNER JOIN association
ON stud.roll_num = association.stud_id;
###########
SELECT stud.roll_num, stud.name, stud.email, association.course_id
FROM stud
LEFT JOIN association
ON stud.roll_num = association.stud_id;

###############
SELECT stud.roll_num, stud.name, stud.email, association.course_id
FROM stud
RIGHT JOIN association
ON stud.roll_num = association.stud_id;

###############
SELECT stud.roll_num, stud.name, stud.email, association.course_id
FROM stud
LEFT JOIN association
ON stud.roll_num = association.stud_id

UNION

SELECT stud.roll_num, stud.name, stud.email, association.course_id
FROM stud
RIGHT JOIN association
ON stud.roll_num = association.stud_id;


#########
SELECT stud.roll_num, stud.name, association.course_id
FROM stud
CROSS JOIN association;

####################