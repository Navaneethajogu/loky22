use college;
 select * from students;
 insert into students ( branch) values("A"),("B"),("C");
 select * from students;
 select max(marks) from students;
 select max(marks) from students where branch="A";
 select max(marks) from students group by branch;
 select branch, max(marks) from students group by branch;
 select branch from students group by branch;
 select branch from students ;
 select branch, max(marks) as max_marks from students group by branch having max_marks>= 70;
 select * from students;





 use college;
desc lokesh;
 select * from lokesh;
 update lokesh set marks=70 where rull_num = 1;
 select * from lokesh;
 update lokesh set marks=80 where rull_num = 3;
 select * from lokesh;
 insert into lokesh (rull_num, name ,section) values(4,"loky",90);
 select * from lokesh;
 desc lokesh;
 select * from lokesh;
 update  lokesh set section="D" where rull_num=5;
 update  lokesh set marks=60 where rull_num=5;
 insert into lokesh (rull_num, name) values ( 6,"rishi");
  update lokesh set section="A", marks=70 where rull_num=6;
 