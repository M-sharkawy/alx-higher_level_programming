-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id),
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
