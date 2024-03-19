Nama: Erista Disti Kirani 

Summary Relational Database 

Database Relationship 

One to one

satu user hanya memiliki 1 foto profil

One to many

satu user bisa memiliki banyak tweets 

Many to many 

satu user bisa banyak follower user, satu user bisa di follow banyak user

Relational Datababse management System (RDBMS) 

software yang menggunakan Relational Database Model sebagai dasarnya contoh: MySQL 


Jenis Perintah SQL 

DDL - Data Definition Language 

DML - Data Manipulation Langugae 

DCL - Data Control Language 

DDL statement 

Create database database\_name; 

Use database\_name; 

create table … 

drop table …

rename table …

Create Table With is Schema 

Create Table table\_name(

column1 data\_type PRIMARY KEY

column2 data\_type FOREIGN KEY, 

…

column data\_type, 

PRIMARY KEY (one or more columns) 

); 

Modify Table Schema 

Alter Table table\_name 

Add Column column\_name 

data\_type; 

Tipe DataMySQL 

Num, Huruf, Date 

DML (Data Manipulation Language 

perintah yang digunakan untuk memanipulasi data dalam tabel dari suatu database 

Statement Operation: 

Insert 

Select 

Update 

Delete 

DML Statement: 

Like / Between 

And / OR 

Order by 

Limit 

Join 

join sebuah klausa untuk mengkombinasi record dari dua atau lebih tabel 

join standar SQL ANSI inner - left - right 

inner join - akan mengembalikan baris - baris dari dua tabel atau lebih yang memenuhi syarat. 

left join - left join akan mengembalikan seluruh baris dari tabel disebelah kiri yang dikenai kondisi ON dan hanya baris dari tabel disebelah kanan yang memenuhi kondisi join. 

Right Join 

Right join akan mengembalikan semua baris dari rabel sebelah kanan yang dikenai kondisi ON dengan data dari tabel sebelah kiri yang memenuhi kondisi join. Teknik ini merupakan kebalikan dari left join. 

Ada hal yang perlu diperhatikan dari union adalah jumlah field yang dikeluarkan/dipanggil harus sama. 

Fungsi Agregasi 

fungsi di mana nilai beberapa baris dikelompokkan bersama untuk membentuk nilai ringkasan tunggal 

Min, Max, Sum, AVG, Count, Having 

Min: fungsi dimana nilai beberapa baris dikelompokkan bersama untuk membnetuk nilain ringasakan tunggal. 

Max: Digunakan untuk mendapatkan nilai maximum atau nilai terbesar dari sebuah data record di tabel. 

Sum: Digunakan untuk mendapatkan jumlah total nilai dari sebuah data atau record di tabel. 

AVG: Digunakan mencari nilai rata-rata (average) dari sebuah data atau record di tabel. 

Count: Digunakan untuk mencari jumlah dari sebuah data atau record di tabel. 

Having: Digunakan untuk menyeleksi data berdasarkan kriteria tertentu. dimana kriteria berupa fungsi aggregat. 



Subquery atau inner query atau nested query adalah query di dalam query SQL lain 

subquery digunakan untuk mengembalikan data yang akan digunakan dalam query utama sebagai syarat lebih membatasi data yang akan di ambil. Subquery dapat digunakan dengan Select, Insert, Update, dan Delete statements bersama dengan operator seperti IN, between, dll. 


