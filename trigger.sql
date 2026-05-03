
use college;
select * from lokesh;

create table loky_act_log (name varchar(100),update_marks int,pre_marks int, time datetime);
create trigger loky_update_trigger after update on lokesh for each row insert into loky_act_log values(new.name,new.marks,old.marks,now());
update lokesh set marks=90 where rull_num_=1;
select * from lokesh;
select*from loky_act_log;
