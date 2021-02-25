# Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

Project requires building an ETL pipeline to extracts their data from S3, stage it in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## Project Description

Apply learnings of data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. Load data from S3 buckets to staging tables on Redshift and execute SQL statements that create the analytics tables(Fact & Dimension) from these staging tables.

## Project Datasets

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data
Log data json path: s3://udacity-dend/log_json_path.json


## Schema for Song Play Analysis

### Staging Tables

* staging_events - Copies the data from LOG_DATA
* staging_songs - Copies the data from SONG_DATA

### Fact Table

* songplays - records in event data associated with song plays

### Dimension Tables

* users- in the app
* songs - in music database
* artists- in music database
* time- timestamps of records in songplays broken down into specific units

## Project Design

Created schemas for staging table and designed the star schema which is to be used by analytics team. Built an ETL pipeline to extract and copy data from S3 buckets to staging tables , transform it and load it in Final tables (used for analytics or reports). 

### Scripts

There are 3 python scripts with desicription as below :

* "create_tables.py" - This is the script to be executed to drop and create tables , please note this script uses "sql_queries.py" for only dropping and creating tables  
* "sql_queries.py" - This scipt is used by other 2 python scripts for DROP, CREATE, INSERT and COPY statements
* "Etl.py" - This script is used to extract & copy data into staging tables and then insert to analytics tables.



## Instructions

1. In Jupyter notebook "NoteBook.ipynb" first step is to import all required libraries
2. Update the configuration file to create the Redshift Cluster.
3. Initialize the services using boto3.
4. Verify the files in provided the S3 buckets.
5. Created the IAM role, attached policy to give read access to S3 buckets.
6. Created redshift cluster and updated the endpoint and role details in the config file.
7. Authorize Security Access Group to Default TCP/IP Address
8. Connect to RDS postgress database.
9. Run create table script "%run create_tables.py".
10. Run ETL pipeline "%run etl.py".
11. Check count of records in each table ( staging & analytics).
12. Run analytics queries for stats ex. Get Most popular song  ( Maximum entries in Fact table) , Get most popular Artist ( artist listnened by distinct users).
13. Delete the cluster and roles.
