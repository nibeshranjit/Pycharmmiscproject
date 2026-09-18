/* SQL practise set 1 */
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

INSERT INTO cars (brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

SELECT * FROM cars;

SELECT brand, year FROM cars;

ALTER TABLE cars ADD color VARCHAR(255);

UPDATE cars
SET color = 'red'
WHERE brand = 'Volvo';
SELECT * FROM cars;

SET color = 'red'
WHERE brand = 'Ford';


ALTER TABLE cars
DROP COLUMN color;

DELETE FROM cars
WHERE brand = 'Volvo';

DROP TABLE cars;

ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4);

SELECT * FROM cars;

/*SQL 2 */

SELECT customer_name, country FROM customers;

SELECT DISTINCT country FROM customers;

SELECT COUNT(DISTINCT country) FROM customers;

SELECT * FROM customers
WHERE city = 'London';

SELECT * FROM products
ORDER BY price;

SELECT * FROM products
ORDER BY price DESC;

SELECT * FROM customers
LIMIT 20;

SELECT * FROM customers
LIMIT 20 OFFSET 40;

SELECT MIN(price)
FROM products;

SELECT MAX(price)
FROM products;

SELECT MIN(price) AS lowest_price
FROM products;

SELECT COUNT(customer_id)
FROM customers;

SELECT COUNT(customer_id)
FROM customers
WHERE city = 'London';

SELECT SUM(quantity)
FROM order_details;

SELECT AVG(price)
FROM products;

SELECT AVG(price)::NUMERIC(10,2)
FROM products;

/*SQL 3*/

SELECT * FROM customers
WHERE customer_name LIKE 'A%';

SELECT * FROM customers
WHERE customer_name LIKE '%a%'; /*case sensitive*/

SELECT * FROM customers
WHERE customer_name LIKE '%en';

SELECT * FROM customers
WHERE city LIKE 'L_nd__';



/*sql 7*/
create table fruits(name varchar(255));

insert into fruits values('apple'),('apple'),('orange'),
 ('grapes'),('grapes'),('watermelon');


select name, ROW_NUMBER() OVER(ORDER BY name) from fruits;

select name, RANK() OVER(ORDER BY name) from fruits;

select name, DENSE_RANK() OVER(ORDER BY name) from fruits;

CREATE TABLE ExamResult
(StudentName VARCHAR(70),
Subject 	VARCHAR(20),
Marks   	INT
);
INSERT INTO ExamResult
VALUES
('Lily',
'Maths',
65
);
INSERT INTO ExamResult
VALUES
('Lily',
'Science',
80
);
INSERT INTO ExamResult
VALUES
('Lily',
'english',
70
);
INSERT INTO ExamResult
VALUES
('Isabella',
'Maths',
50
);
INSERT INTO ExamResult
VALUES
('Isabella',
'Science',
70
);
INSERT INTO ExamResult
VALUES
('Isabella',
'english',
90
);
INSERT INTO ExamResult
VALUES
('Olivia',
'Maths',
55
);
INSERT INTO ExamResult
VALUES
('Olivia',
'Science',
60
);
INSERT INTO ExamResult
VALUES
('Olivia',
'english',
89
);

Select * from examrest

SELECT Studentname,
   	Subject,
   	Marks,
   	ROW_NUMBER() OVER(ORDER BY Marks) RowNumber
FROM ExamResult;


SELECT Studentname,
   	Subject,
   	Marks,
   	ROW_NUMBER() OVER(ORDER BY Marks) RowNumber
FROM ExamResult;












