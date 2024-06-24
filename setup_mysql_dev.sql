-- Script creates a new database named hbnb_dev_db
-- A new user hbnb_dev in localhost
-- hbnb_dev user password set hbnb_dev_pwd
-- hbnb_dev user to have all privileges on database hbnb_dev_db
-- hbnb_dev user to have SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';