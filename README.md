# Postgresql-Database-Migration-Python
The aim of project is to make migration of postgreSQL db using python alembic tool. In this project, first students and interest table were created. Then columns from students and interest table updated and migrated accordingly. 
To use this project u need to have Postgresql, Python, Alembic, Psycopg2 installed in ur comp. 
Python is connected to Postgres DB Server. Using Psycopg2 database adapter, sample table data has been created. Alembic used to generate  migration and rollback script. 
HOW TO USE THE PROGRAM  ?
  U may clone the project directly. After running py codes u should be able to see tables in PgAdmin4. Just fyi: user name:postgres, pw: root, host is localhost as usual, port number is default.5432. name of db: 'stdb'
  1. To initialize alembic: 
  Type this in project folder where also alembic installed : "alembic init alembic" This will initalize and create alembic files in alembic folder.
  2. Format sqlalchemy url. For my project I formatted it like this: " sqlalchemy.url = postgres://postgres:root@localhost/stdb" 
  3. To check above u may run this in terminal : "alembic current"
  4. To create revision( migration code) just type this "alembic revision -m "Some comment\name of ur migration"  "
  in terminal and it will create .py file in alembic/version directory. 
  5. in the created file , in upgrade function write ur migration script, and in dowgrade function write ur rollback script. For more info refer to this link : https://alembic.sqlalchemy.org/en/latest/tutorial.html
  6. To make migration happen type this in terminal : 
  "alembic upgrade head"
  7. To undo migration (to rollback)  write this in terminal
  "alembic downgrade -1"
  If for some reason rollback doesnt take place, u may just look at revision history by typing "alembic history" and by refering to file name u might do it manually for example: 
  " alembic downgrade dfea060dfde4"
