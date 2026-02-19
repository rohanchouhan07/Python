CREATE DATABASE shopdb;
use shopdb;
Create Table Customer (
customer_id int auto_increment primary key,
Name varchar(100),
Age int(2),
Gmail varchar(50),
City varchar(20)
);

INSERT INTO customer (Name,Age,Gmail,City) values
('Rohan',22,'Rohan@gmail.com',"Indore"),
('Divya',20,'Divya@gmail.com',"Pune"),
('Harsh',19,'Harsh@gmail.com',"Ujjain"),
('Neha',23,'Neha@gmail.com',"Delhi");

Select * from customer;
Select Name from customer;
Select Name,City from customer;
SELECT CITY FROM CUSTOMER WHERE NAME='Rohan';
SELECT CITY FROM CUSTOMER WHERE NAME='N%%%%' AND GMAIL='NEHA@GMAIL.COM';

-- SORTING --  
SELECT * FROM customer ORDER BY customer_id DESC;
SELECT * FROM customer ORDER BY NAME ASC;

#Disable safe mode  
SET SQL_SAFE_UPDATES = 0;

 
-- UDATE COLUMNS-- 
UPDATE customer SET City="BHOPAL" WHERE City="Indore";

-- DELETE COLUMNS-- 
DELETE FROM CUSTOMER WHERE NAME="HARSH";