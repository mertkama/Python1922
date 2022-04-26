CREATE TABLE contacts(
    contact_id serial PRIMARY KEY ,
    account_id INT,
    contact_name VARCHAR NOT NULL ,
    pohone varchar(15) UNIQUE,
    email varchar(100) UNIQUE,

    CONSTRAINT FK_ACOUNTS
                     FOREIGN KEY (account_id)
                     REFERENCES accounts(user_id)
);

INSERT INTO contacts(account_id, contact_name, pohone, email)
values (3,'Ahmet Aslan','222 222 22 22', 'ahmet@aslan.com');

-- Yanlış kullanım
SELECT *
FROM accounts
         LEFT JOIN contacts c on accounts.user_id = c.account_id
where  accounts.user_id = 1;

-- Doğru kullanım
SELECT  c.contact_name,  c.email,  c.pohone
FROM contacts as c
        left join accounts a on a.user_id =  c.account_id
where a.user_id = 1;


select *
from contacts
INNER JOIN accounts a on a.user_id = contacts.account_id
WHERE contacts.account_id = 1 ORDER BY  contacts.contact_id desc;


select *
from contacts
RIGHT JOIN accounts a on a.user_id = contacts.account_id;






CREATE TABLE employee (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	manager_id INT,
	FOREIGN KEY (manager_id)
	REFERENCES employee (employee_id)
	ON DELETE CASCADE
);


INSERT INTO employee (
	employee_id,
	first_name,
	last_name,
	manager_id
)
VALUES
	(1, 'Windy', 'Hays', NULL),
	(2, 'Ava', 'Christensen', 1),
	(3, 'Hassan', 'Conner', 1),
	(4, 'Anna', 'Reeves', 2),
	(5, 'Sau', 'Norman', 2),
	(6, 'Kelsie', 'Hays', 3),
	(7, 'Tory', 'Goff', 3),
	(8, 'Salley', 'Lester', 3);



select concat(e.first_name, ' ', e.last_name) employee,
        concat(m.first_name, ' ', m.last_name) manager
from employee e
INNER JOIN employee m on m.employee_id = e.manager_id;

DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;


-- FULL OUTER JOIN
CREATE TABLE departments (
	department_id serial PRIMARY KEY,
	department_name VARCHAR (255) NOT NULL
);

CREATE TABLE employees (
	employee_id serial PRIMARY KEY,
	employee_name VARCHAR (255),
	department_id INTEGER
);

INSERT INTO departments (department_name)
VALUES
	('Sales'),
	('Marketing'),
	('HR'),
	('IT'),
	('Production');


INSERT INTO employees (
	employee_name,
	department_id
)
VALUES
	('Bette Nicholson', 1),
	('Christian Gable', 1),
	('Joe Swank', 2),
	('Fred Costner', 3),
	('Sandra Kilmer', 4),
	('Julia Mcqueen', NULL);

SELECT * FROM  departments;
SELECT * FROM employees;

SELECT e.employee_name, d.department_name FROM employees  as e

full outer join departments d
    on d.department_id = e.department_id
where department_name is not null and e.department_id is not null;


SELECT e.employee_name, d.department_name FROM employees  as e

full outer join departments d
    on d.department_id = e.department_id
where department_name is  null and e.department_id is  null;
