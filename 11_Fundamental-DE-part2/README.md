Summary Fundamental DE Part2 

The type of data based on its schema: structured and unstructured data 

How the data is stored based on its type: Relational vs noSQL database 

Type of database: OLTP vs OLAP 

The difference between database, data lake, data warehouse, data mart 

What is Structure Data 

- Structured data is data that has a defined data model, format and schema, such as: fields as name, address, zip code. it is stored in relational database (RDBMS) and easily searched through SQL (Structured Query Language). 
- Estimated 20% of enterprise data 
- Requires less storage 

What is Unstructures Data

- Unstructured data is data that has internal structure but is not structure via pre-defined data models or schemas. Unstructrure data does not fit nicely into relational database like SQL and need advanced processing to make it searchable. 
- Example: 

  `	`- Text documents, pdf, images, Video

  `	`- Social media: data from twitter, facebook, instagram 

  Estimated 80% of enterprise data 

  Requires more storage 

Relational Database 

`	`A relational database is a collection of data items with pre-defined relationships between them. 

Database Normalization 

- Database normalization is a database design principle for organizing data in an organized and consistent way. 
- The main purpose of database normalization is to void complexities, eliminate duplicates, maintain the integrity of the database and organize data in consistent way. In normalization, the data divided into several tables linked together with relationships. 
- It also helps you eliminate undesirable characteristic associated with insertion, deletion, and updating. 

NoSQL Databse 

- NoSQL databases supports more semi-structured data have flexible schemas for building modern application. 
- NoSQL database are typically distributed system where several machines work together  in cultures. 

Advantages & Disadvantages of Key-Value DB 

Advantages 

- Fastt read and write performance 
- Easy to use and integrate into existing application 
- Flexible to store various types of data: scalar to complex object 

Disadvantages 

- Limited querying capabilities, particularly complex queries or joins 
- Support only simple data model and not support relationships 

NoSQL: Wide-Coloumn DB 

- A type of NoSQL database that stores data in a coloumn-family format within a distributed system architecture. 
- it use tables, rows, and columns, but unlike relational database, the names and format of the columns can vary from row to row in the same table. 

OLTP vs OLAP 

- Types of database based on the purpose of the query (transaction/analytical): OLTP and OLAP 
- RDBMS is good to maintain OLTP use cases. OLTP (Online Transaction Processing) is a data processing category that deals with numerous transaction performed users that involve inserting, updating, and deleting data. 
- Data warehouse is good to maintain OLAP (Online analytical processing) us cases: to answer multi-dimensional analytical queries. 

Data Lake 

- Data Lake is a centerlized repository designed to store, process, and secure large amounts of semi-structured and unstrucctured data. 
- It can store data its native format and process any variety of it, ignoring size limits. 
- Tools: Amazon, Google Cloud Storage 


