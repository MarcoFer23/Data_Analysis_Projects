/* One basic exercise to practice database and table creation.
Let's create a videogame store databse, and fill it with dedicated tables: */

CREATE DATABASE videogames;

USE videogames;

CREATE TABLE Store (
    store_id INT AUTO_INCREMENT,
    store_address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    PRIMARY KEY (store_id)
);

CREATE TABLE Employee (
    tax_id_num VARCHAR(16),
    full_name VARCHAR(255) NOT NULL,
    degree VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    job VARCHAR(255) NOT NULL,
    store_id INT NOT NULL,
    hire_date DATE NOT NULL,
    employment_termination_date DATE,
    PRIMARY KEY (tax_id_num),
    CONSTRAINT FK_store_employee FOREIGN KEY (store_id)
        REFERENCES Store (store_id)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE Department (
    store_id INT,
    department_id INT,
    PRIMARY KEY (store_id , department_id),
    CONSTRAINT FK_store_department FOREIGN KEY (store_id)
        REFERENCES Store (store_id)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE Videogames (
    game_id INT AUTO_INCREMENT,
    title VARCHAR(255),
    developer VARCHAR(255),
    release_year INT NOT NULL,
    price DECIMAL(5 , 2 ) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    remake BOOLEAN NOT NULL,
    PRIMARY KEY (game_id)
);


CREATE TABLE Location (
    store_id INT,
    game_id INT,
    department_id INT,
    position VARCHAR(255) NOT NULL,
    available BOOLEAN NOT NULL,
    title VARCHAR(255) NOT NULL,
    developer VARCHAR(255) NOT NULL,
    PRIMARY KEY (store_id , department_id , title , developer),
    CONSTRAINT FK_store_location FOREIGN KEY (store_id)
        REFERENCES Store (store_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    CONSTRAINT FK_store_department_location FOREIGN KEY (store_id , department_id)
        REFERENCES Department (store_id , department_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    CONSTRAINT FK_videogame_id FOREIGN KEY (game_id)
        REFERENCES Videogames (game_id)
        ON UPDATE CASCADE ON DELETE NO ACTION
);