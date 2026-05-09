use college;
select * from lokesh;
select name,marks,if(marks>80 ,'selected' ,'rejected') as results from lokesh where marks>80;
select name,marks,if(marks>80 ,'selected' ,'rejected') as results from lokesh where marks<=80;
select name,marks,if(marks>80 ,'selected' ,'rejected') as results from lokesh ;
select name,marks,
case
when marks>80 then 'selected'
when marks between 60 and 70 then'under process'
else 'rejected'
end as status
from lokesh;