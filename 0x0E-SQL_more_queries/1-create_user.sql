--  creates the MySQL server user user_0d_1
CREATE USER if NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- user_0d_1 have all privileges
GRANT * ON database.* TO 'user_0d_1'@'localhost';
