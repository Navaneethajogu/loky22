se college;
 CREATE TABLE priya (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    marks INT CHECK (marks >= 0),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);
select * from priya;
use college;
 select*from priya;
 insert into priya values ( 2,'neetha','loky729@gmail.com',90 ,'hydreabad');
 select*from priya;
 insert into priya values ( 3,'nee','budige vaa729@gmail.com',92 );