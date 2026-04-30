mysql> CREATE DATABASE college;
Query OK, 1 row affected (0.02 sec)

mysql> USE college;
Database changed
mysql> CREATE TABLE students(
    -> id INT PRIMARY KEY,
    -> name VARCHAR(50),
    -> age INT,
    -> course VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> INSERT INTO students VALUES (1,'Ravi',20,'BSc');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO students VALUES (2,'Priya',21,'BCom');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (3,'Rahul',22,'BCA');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (4,'Sneha',20,'BBA');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (5,'Arjun',21,'BTech');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (6,'Kiran',22,'BSc');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (7,'Divya',20,'BCA');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (8,'Manoj',23,'BCom');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (9,'Anjali',21,'BBA');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO students VALUES (10,'Vikram',22,'BTech');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM students;
+----+--------+------+--------+
| id | name   | age  | course |
+----+--------+------+--------+
|  1 | Ravi   |   20 | BSc    |
|  2 | Priya  |   21 | BCom   |
|  3 | Rahul  |   22 | BCA    |
|  4 | Sneha  |   20 | BBA    |
|  5 | Arjun  |   21 | BTech  |
|  6 | Kiran  |   22 | BSc    |
|  7 | Divya  |   20 | BCA    |
|  8 | Manoj  |   23 | BCom   |
|  9 | Anjali |   21 | BBA    |
| 10 | Vikram |   22 | BTech  |
+----+--------+------+--------+
10 rows in set (0.00 sec)

mysql>