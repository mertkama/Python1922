-- DDL (Data Definition Language)
--
-- create  -> OLUŞTURMA
-- alter   -> GÜNCELLEME
-- drop    -> SİLME

-- TABLO OLUŞTURMA
create table  accounts(
    user_id serial PRIMARY KEY ,
    user_name VARCHAR(50) UNIQUE NOT NULL ,
    password VARCHAR(50) NOT NULL ,
    email VARCHAR(100) UNIQUE NOT NULL ,
    created_on TIMESTAMP NOT NULL ,
    last_login timestamp
);

-- TABLOYA VERİ EKLEME
INSERT INTO  accounts(user_name, password, email, created_on, last_login)
VALUES ('mehmet_nuri', 'denemeşifre','info@mehmetnuri.net', current_timestamp, current_timestamp );

INSERT INTO  accounts(user_name, password, email, created_on, last_login)
VALUES ('omer_yavuz', 'bosnak_34','omer@yavuz.com', current_timestamp, current_timestamp );

INSERT INTO  accounts(user_name, password, email, created_on, last_login)
VALUES ('kadiye_aslan', 'kaslan34','kaslan@aslan.com', current_timestamp, current_timestamp );

insert into accounts (user_name, password, email, created_on, last_login)
values('hatice_kalkan', 'hkalkan55', 'hkalkan@kalkan.com', current_timestamp, current_timestamp);


-- VERİ ÇEKME

SELECT * FROM accounts;  -- BÜTÜN KOLONLARI GETİRİR

SELECT user_name, email, user_id FROM accounts; -- BELİRLİ KOLONLARI GETİRİR

SELECT * FROM  accounts WHERE   user_id = 1;
SELECT * FROM  accounts WHERE   user_name = 'kadriye_aslan';      -- tam eşit olanı ara
SELECT * FROM accounts  WHERE   user_name LIKE '%kadriye_aslan%';   --içerisinde ara
SELECT * FROM accounts  WHERE   user_name LIKE 'kadriye%';         -- ile başlayanları ara
SELECT * FROM accounts  WHERE   user_name LIKE '%aslan';         -- ile bitenleri ara
SELECT * FROM accounts  WHERE   user_name  IS NOT NULL AND user_name LIKE '%aslan' ; --birden fazla koşul belirtme
SELECT * FROM  accounts WHERE   user_id > 1;
SELECT * FROM  accounts WHERE  user_id IN(1,4,5);
SELECT * FROM  accounts WHERE  user_id BETWEEN 3 AND 5;
SELECT * FROM  accounts WHERE  user_id = 1 OR user_id = 10;
SELECT * FROM  accounts WHERE  user_id <> 1 ;
SELECT * FROM  accounts WHERE  user_id != 1 ;
SELECT * FROM  accounts WHERE  user_id IS NOT NULL ;
SELECT * FROM  accounts WHERE  user_id >=2;
SELECT * FROM  accounts WHERE  user_id <=3;
SELECT * FROM  accounts WHERE  length(user_name) between 1 and 11 order by user_name asc ; -- a dan z ye sırala
SELECT * FROM  accounts WHERE  length(user_name) between 1 and 11 order by user_name desc ; -- z den a ya sırala


--  TABLOYA YENİ KOLON EKLEME
ALTER TABLE accounts ADD COLUMN birth_year INT;

-- VERİ GÜNCELLEME
UPDATE accounts SET birth_year = 2001 where user_name =  'kadriye_aslan';
update accounts set birth_year = 1900  where birth_year is null;


--TABLO ADI GUNCELLEME
ALTER TABLE hesaplar RENAME TO  accounts;



