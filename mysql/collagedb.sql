CREATE DATABASE IF NOT EXISTS COLLAGEDB;
USE COLLAGEDB;
CREATE TABLE Students(
Studentid int auto_increment primary key,
Name varchar(100),
Age tinyint,
Email varchar(100),
JoinDate Date
);
show tables;
select * from students;
Insert into Students (Name,Age,Email,JoinDate)values
("Ayush Kumar",22,"ayushkumar@gmail.com",'2004-10-20'),
("Krish Verma",21,"krishVerma@gmail.com",'2006-11-22'),
("Divya Kumawat",25,"DivyaKumawat@gmail.com",'2003-12-05');

Alter table Students add column gender varchar(10);
ALter Table Students Rename Column gender to Gender;
Alter Table Students Modify column Age smallint;

create Table Rohan(rohanid int auto_increment primary key,
name varchar(50)
);

truncate Rohan;
drop table Rohan;

