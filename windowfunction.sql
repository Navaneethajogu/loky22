use college;
select*from  lokesh;
select*, rank() over(order by marks desc)as ranks from students;
select*, dense_rank() over(order by marks desc)as ranks from students;
select name,marks,row_number() over() as sno from students;