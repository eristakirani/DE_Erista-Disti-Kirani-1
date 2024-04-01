Nama: Erista Disti Kirani 

Summary Data Warehouse and Data Lake (Part 1) 

Introduction to Data warehouse  

Columnar Table 

Replication + Sharding 

Introduction to Biq Query + GCS 

- Introduction to Data Warehouse 

  Data warehouse is a system that aggregates data from different sources into a single, central, consistent data store to support data analysis, data mining, artificial intelligence (AI), and machine learning. 

- A system 
- Aggrerates data from different sources 
- To support analysis, data mining, AI, and machine learning 

- Data Lake vs Data Warehouse 

  ` `-  A data lake tends to include large amounts of raw data, the purpose for which may not yet be defined 

  - A data warehouse is a repository for structured, filtered data that has already been processed for a specific purpose. 

- Data Lakehouse 

  A data lakehouse is an open data management architecture that combines the flexibility and cost-efficiency of data lakes with the data management and structured features of data warehouse, all on one data platform. 


- Common Technologies for Data Warehouse 

  - AWS Redsgift 

  - Google Big Query 

  - Clickhouse 

  - Snowflake 

  - Databricks 

  - Apache Dorris 

  - Postgree (with Extension) 

  - Etc

- Columnar Table 

  Postgresql Citus Extension 

  What is citus? 

- open sources to postgreSQL extension to PostgreSQL that transform postgres into a distributed database 
- Employes distributed tables, reference tables, and a distributed SQL query engine 

- Citus Advantages 

  ` `-  Distributed tables are shared accros a cluster of PostgreSQL nodes to combine their CPU, memory, storage and I/O capacity 

  - Reference tables are replicated to all nodes for joins and foreign keys from distributed tables and maximum read performance. 

  - Distributed query engine routes parallizes SELECT, DML, and other operations on distributed tables across the cluster. 

  - Columnar storage compresses data, speeds up scans, and supports fast projections, both on regular and distributed tables. 

  - Query from any enables you to utilize the full capacity of your cluster for distributed queries. 

Columnar Tables 

- The data is stored in column-oriented instead of row-oriented structure
- Disadvantages 

  - Slower write time

- Advantages 

  - Better access time 

  - Compression 

Replication + Sharding 

- Sharding 

  -  The data is chunked into several parts and distributed among multiple nodes 

  - Used for Distributed processing/storage 

  - Youcan store data larger than node capacity

- Replication 

  - The same data copied among multiple nodes 

  - Used for backup/high availability 

Introduction to Big Query & GCS 

Google Cloud Platform 

Cloud platform provide multiples service and infrastructure, so that companies dont have to provide everything by themselves. 

Some well known cloud platform

- GCP 
- AWS 
- Azure 
- Ali cloud 

