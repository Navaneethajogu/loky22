use college;
select name,marks from students where marks<(select max(marks) from students);
select * from students where marks=(select max(marks) from students);
select max(marks) from students where marks<(select max(marks) from students);
select max(marks) from students where marks<(select max(marks) from students where marks<(select max(marks) from students));
