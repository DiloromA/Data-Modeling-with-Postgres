## Data Modeling with Postgres
### Summary
Sparkify is a fictitious online music streaming company, where data about songs, users and artists are stored. 
This project involves data modeling of Sparkify data using Postgres. The goal of the project is to extract data from multiple sources, transform and model the data, and build an ETL pipeline. The application processes 72 song_data files and 30 log_data files. 

### Files
- **Data** - folder where data is located.
- **create_tables.py** - Python script where create database, create table and drop table code is located.
- **etl.ipynb** - Jupiter file where code to prepare ETL process is located.This is a preparatory script to use in **etl.py** script later.
- **etl.py** - Python script to extract, transform and load data from the sources to the server tables.
- **README.md** - file containing project information.
- **sql_queries.py** - Python script where create tables, insert and drop tables code is located.
- **test.ipynb** - Jupyter file to validate ETL code results. 

### Database schema
![database_schema_diagram](database_schema_diagram.png)

### Instructions
To run the program:
1. Open the Terminal,
2. Run "python create_tables.py" on the Terminal,
3. Run "python etl.py" on the Terminal
4. Open **test.ipynb** and run each cell. 

### Packages used
1. psycopg2
2. os
3. glob
4. pandas


