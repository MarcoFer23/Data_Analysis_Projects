/* 

Here is a simplified database schema (comprising 6 tables in total) for a veterinary clinic located in the Province of Rome,
which treats pets belonging to clients residing in the provinces of Rome, Latina, and Frosinone.

To make it easier to consult the models I used to design the database, below I’ve included links to the associated resources 
available on Canva (please note that the relational model was built in MySQL Workbench through Reverse Engineering --> CTRL + R in Windows).

Access privileges: Anyone with the link CAN COMMENT.

ER Diagram: https://www.canva.com/design/DAFtOKMyT0Q/r8T1lMh1EYaUbYYpuB2diQ/edit?utm_content=DAFtOKMyT0Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Reverse engineered model: https://www.canva.com/design/DAFtOGZ_HVk/snS4X5j3VIDuFRng4W0mcQ/edit?utm_content=DAFtOGZ_HVk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

*/

CREATE DATABASE veterinary_clinic_db;

USE veterinary_clinic_db;

CREATE TABLE cities (
    city_id INT AUTO_INCREMENT,
    city_name VARCHAR(255) NOT NULL,
    region VARCHAR(255) NOT NULL,
    county VARCHAR(255) NOT NULL,
    PRIMARY KEY (city_id)
);

CREATE TABLE pet_owners (
    owner_id INT AUTO_INCREMENT,
    city_id INT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    email_address VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (owner_id),
    CONSTRAINT FK_city_id_pet_owner_city FOREIGN KEY (city_id)
        REFERENCES cities (city_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE INDEX idx_pet_owners_cities ON pet_owners (city_id);

CREATE TABLE veterinarians (
    veterinarian_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    graduation_date DATE NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10 , 2 ) NOT NULL CHECK (salary > 0),
    PRIMARY KEY (veterinarian_id)
);

CREATE TABLE species (
    species_id INT AUTO_INCREMENT,
    species_name VARCHAR(255) NOT NULL,
    common_name VARCHAR(255) NOT NULL,
    genus VARCHAR(255) NOT NULL,
    family VARCHAR(255) NOT NULL,
    phylum VARCHAR(255) NOT NULL,
    PRIMARY KEY (species_id)
);

CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT,
    owner_id INT NOT NULL,
    species_id INT NOT NULL,
    pet_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    neutered BOOLEAN NOT NULL DEFAULT 0,
    pet_weight_kg DECIMAL(5 , 2 ) NOT NULL CHECK (pet_weight_kg > 0),
    PRIMARY KEY (pet_id),
    CONSTRAINT FK_ID_pets_pet_owners FOREIGN KEY (owner_id)
        REFERENCES pet_owners (owner_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FK_ID_pets_species FOREIGN KEY (species_id)
        REFERENCES species (species_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE INDEX idx_pets_pet_owners ON pets (owner_id);
CREATE INDEX idx_pets_species ON pets (species_id);

CREATE TABLE visits (
    visit_serial INT AUTO_INCREMENT,
    pet_id INT NOT NULL,
    veterinarian_id INT NOT NULL,
    visit_date DATETIME NOT NULL,
    PRIMARY KEY (visit_serial),
    CONSTRAINT FK_ID_visits_pets FOREIGN KEY (pet_id)
        REFERENCES pets (pet_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT FK_ID_visits_veterinarians FOREIGN KEY (veterinarian_id)
        REFERENCES veterinarians (veterinarian_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE INDEX idx_visits_pets ON visits (pet_id);
CREATE INDEX idx_visits_veterinarians ON visits (veterinarian_id);

-- Adding values to tables (without manually adding IDs to let auto_increment work when inserting values):

INSERT INTO cities (city_name, region, county)
VALUES
	('Albano Laziale', 'Lazio', 'RM'),
	('Artena', 'Lazio', 'RM'),
	('Bassiano', 'Lazio', 'LT'),
	('Carpineto Romano', 'Lazio', 'RM'),
	('Cori', 'Lazio', 'LT'),
	('Ferentino', 'Lazio', 'FR'),
	('Frosinone', 'Lazio', 'FR'),
	('Isola dei Liri', 'Lazio', 'FR'),
	('Latina', 'Lazio', 'LT'),
	('Nemi', 'Lazio', 'RM'),
	('Norma', 'Lazio', 'LT'),
	('Rocca Massima', 'Lazio', 'LT'),
	('Roccasecca', 'Lazio', 'FR'),
	('Roma', 'Lazio', 'RM'),
	('Sermoneta', 'Lazio', 'LT');
   
INSERT INTO pet_owners 
(city_id, first_name, last_name, birth_date, email_address, phone_number, address)
VALUES
(11,'Marco','Rossi','1994-03-12','marco.rossi@gmail.com','3514620460','Via del Boschetto, 14'),
(6,'Laura','Bianchi','2002-07-25','laura.bianchi@outlook.it','3469876543','Vicolo dei Pini, 56'),
(7,'Simone','Ricci','1983-11-08','simone.ricci@yahoo.com','3345678901','Piazza del Sole, 89'),
(8,'Anna','Martini','2007-01-19','anna.martini@gmail.com','3502345678','Corso delle Rose, 34'),
(13,'Luca','Ferrari','1988-05-30','luca.ferrari@libero.it','3478765432','Largo dei Ciliegi, 72'),
(3,'Giulia','Russo','2004-09-14','giulia.russo@yahoo.com','3514567890','Viale delle Palme, 45'),
(5,'Paolo','Conti','1993-02-21','paolo.conti@gmail.com','3463456789','Via delle Viole, 17'),
(9,'Sara','Santoro','1985-06-17','sara.santoro@outlook.it','3347890123','Piazza della Luna, 98'),
(11,'Davide','Romano','1999-12-03','davide.romano@gmail.com','3505678901','Vicolo delle Orchidee, 21'),
(12,'Valentina','Gatti','2006-04-11','valentina.gatti@yahoo.com','3476789012','Corso dei Gigli, 63'),
(15,'Antonio','Moretti','1990-08-09','antonio.moretti@libero.it','3512345678','Largo delle Azalee, 37'),
(1,'Francesca','De Luca','1997-10-27','francesca.deluca@gmail.com','3468901234','Viale dei Papaveri, 81'),
(2,'Lorenzo','Barbieri','1982-03-05','lorenzo.barbieri@outlook.it','3346789012','Via delle Mimose, 29'),
(4,'Marta','Ferri','2001-07-18','marta.ferri@yahoo.com','3501234567','Piazza delle Stelle, 52'),
(10,'Giovanni','Marchetti','1994-01-30','giovanni.marchetti@gmail.com','3472345678','Corso delle Tulipani, 76'),
(14,'Elena','Rizzo','1986-09-22','elena.rizzo@libero.it','3515678901','Largo dei Girasoli, 42'),
(1,'Andrea','Lombardi','2005-02-14','andrea.lombardi@gmail.com','3464567890','Vicolo dei Narcisi, 15'),
(2,'Roberta','Colombo','1989-11-01','roberta.colombo@outlook.it','3342345678','Viale delle Ortensie, 69'),
(4,'Michele','Monti','1998-06-10','michele.monti@yahoo.com','3507890123','Via dei Rododendri, 23'),
(10,'Claudia','Villa','1981-12-19','claudia.villa@gmail.com','3477890123','Piazza dei Fiori, 58'),
(14,'Fabio','Ferrara','2003-03-28','fabio.ferrara@libero.it','3516789012','Corso delle Camelie, 31'),
(3,'Giorgia','Pellegrini','1992-08-06','giorgia.pellegrini@gmail.com','3465678901','Largo delle Peonie, 74'),
(5,'Alessandro','Rossetti','2008-05-12','alessandro.rossetti@yahoo.com','3341234567','Vicolo dei Lillà, 67'),
(9,'Eleonora','Galli','1991-10-03','eleonora.galli@outlook.it','3508901234','Via delle Azalee, 38'),
(11,'Nicolas','Russo','2000-04-07','nicolas.russo@gmail.com','3473456789','Piazza delle Margherite, 91');

INSERT INTO veterinarians 
(first_name, last_name, birth_date, graduation_date, hire_date, salary)
VALUES
	('Mario','Bianchi','1989-04-12','2015-06-15','2016-03-20',50000),
	('Laura','Bonicalzi','1996-08-25','2022-09-10','2023-07-12',45000),
	('Luca','Marini','1982-01-30','2009-03-25','2010-11-08',55000),
	('Giulia','De Benedettis','1991-07-19','2014-11-30','2016-02-14',48000),
	('Andrea','Morosini','1987-10-05','2013-07-18','2015-05-01',52000),
	('Sofia','Cangemi','1994-03-11','2018-05-22','2019-09-03',47000),
	('Marco','Tamberi','1979-12-02','2008-09-05','2011-04-19',58000),
	('Elena','Sorrentini','1990-06-27','2014-12-10','2016-08-26',49000),
	('Alessio','Trentini','1985-02-14','2009-04-03','2011-10-15',53000),
	('Serena','Prati','1997-09-09','2018-08-14','2022-06-07',46000);
       
INSERT INTO species (species_name, common_name, genus, family, phylum)
VALUES
	('Canis lupus familiaris', 'Cane', 'Canis', 'Canidae', 'Chordata'),
	('Felis catus', 'Gatto', 'Felis', 'Felidae', 'Chordata'),
	('Oryctolagus cuniculus', 'Coniglio', 'Oryctolagus', 'Leporidae', 'Chordata'),
	('Cricetus cricetus', 'Criceto europeo', 'Cricetus', 'Cricetidae', 'Chordata'),
	('Melopsittacus undulatus', 'Pappagallo ondulato', 'Melopsittacus', 'Psittacidae', 'Chordata'),
	('Testudo graeca', 'Tartaruga greca', 'Testudo', 'Testudinidae', 'Chordata'),
	('Canis familiaris', 'Cane', 'Canis', 'Canidae', 'Chordata'),
	('Felis domesticus', 'Gatto', 'Felis', 'Felidae', 'Chordata'),
	('Lepus europaeus', 'Lepre europea', 'Lepus', 'Leporidae', 'Chordata'),
	('Phodopus sungorus', 'Criceto nano russo', 'Phodopus', 'Cricetidae', 'Chordata');

INSERT INTO pets (owner_id, species_id, pet_name, birth_date, neutered, pet_weight_kg)
VALUES
	(23,7,'Fido','2019-05-15',1,12.5),
	(4,3,'Whiskers','2020-02-10',0,4.2),
	(10,9,'Buddy','2018-08-20',1,9.0),
	(17,2,'Mittens','2021-04-03',0,3.8),
	(6,8,'Luna','2019-11-25',0,5.6),
	(21,4,'Rocky','2020-07-12',1,15.2),
	(2,6,'Charlie','2017-09-08',0,7.9),
	(14,1,'Daisy','2018-01-19',0,6.4),
	(25,5,'Max','2020-06-30',1,8.7),
	(9,10,'Lucy','2019-03-04',0,11.3),
	(19,3,'Oliver','2020-11-14',1,4.5),
	(12,7,'Bella','2018-12-27',0,5.9),
	(1,2,'Leo','2019-08-05',1,10.1),
	(15,9,'Lola','2017-07-01',0,8.0),
	(7,8,'Oscar','2020-09-22',1,6.7),
	(22,1,'Molly','2019-02-17',0,3.3),
	(24,4,'Rosie','2021-01-08',0,9.8),
	(11,5,'Charlie','2018-04-12',1,12.6),
	(18,10,'Sophie','2020-03-27',1,7.1),
	(5,6,'Lucky','2019-06-09',0,14.0),
	(16,7,'Milo','2018-10-31',1,9.4),
	(8,3,'Zoe','2017-12-15',0,5.2),
	(3,2,'Chloe','2020-08-02',0,6.8),
	(13,8,'Coco','2019-04-19',1,7.7),
	(20,9,'Simba','2018-03-08',1,10.9),
	(20,1,'Ruby','2020-10-27',0,8.5),
	(13,4,'Harley','2019-07-13',1,11.7),
	(3,10,'Mia','2018-05-28',0,4.0),
	(8,6,'Zeus','2017-06-04',1,13.2),
	(16,5,'Lily','2019-09-16',0,7.3);

INSERT INTO visits (pet_id, veterinarian_id, visit_date)
VALUES
	(13,7,'2023-01-15 08:30:00'),
	(7,3,'2023-02-20 10:45:00'),
	(23,9,'2023-03-25 14:15:00'),
	(28,5,'2023-04-10 09:00:00'),
	(2,1,'2023-05-05 11:30:00'),
	(20,8,'2023-06-12 16:20:00'),
	(5,4,'2023-07-19 13:00:00'),
	(15,6,'2023-08-08 17:45:00'),
	(29,2,'2023-09-14 10:00:00'),
	(22,10,'2023-10-21 12:30:00'),
	(2,2,'2023-11-26 15:15:00'),
	(19,6,'2023-12-02 08:00:00'),
	(9,4,'2023-04-05 09:30:00'),
	(6,8,'2023-05-10 11:10:00'),
	(23,1,'2023-06-15 14:50:00'),
	(15,5,'2023-07-20 16:25:00'),
	(26,9,'2023-08-25 18:40:00'),
	(11,3,'2023-09-30 07:15:00'),
	(17,7,'2023-10-06 10:20:00'),
	(4,7,'2023-11-11 13:55:00'),
	(16,8,'2023-12-16 15:05:00'),
	(6,4,'2023-02-22 09:25:00'),
	(25,2,'2023-03-30 11:40:00'),
	(26,7,'2023-04-14 14:00:00'),
	(11,10,'2023-05-19 16:10:00');
    
-- Following are some medium-advanced SQL query samples:

-- Display the pet's ID, name, and age, along with the owner's name; sort by pet name.
SELECT 
    p.pet_id,
    p.pet_name,
    TIMESTAMPDIFF(YEAR,
        p.birth_date,
        CURDATE()) AS age,
    o.first_name,
    o.last_name
FROM
    pets AS p
        LEFT JOIN
    pet_owners AS o ON p.owner_id = o.owner_id
ORDER BY pet_name;

-- Display the name and salary of the veterinarian with the highest salary (SQL views).
CREATE VIEW veterinarian_max_salary AS
    SELECT 
        CONCAT(first_name, ' ', last_name) AS vet_full_name, salary
    FROM
        veterinarians
    WHERE
        salary = (SELECT 
                MAX(salary)
            FROM
                veterinarians);

SELECT 
    *
FROM
    veterinarian_max_salary;
    
-- Display the ID and name of pets, along with the scientific name, genus, and common name of the species for all pets whose genus is not Canis or Felis.
SELECT 
    p.pet_id, p.pet_name, s.species_name, s.genus, s.common_name
FROM
    pets AS p
        LEFT JOIN
    species AS s ON p.species_id = s.species_id
WHERE
    s.genus NOT IN ('Canis' , 'Felis')
ORDER BY p.pet_id;

-- Display the ID, name, date of birth, and owner's name for pets belonging to people whose names begin with M.
SELECT 
    p.pet_id,
    p.pet_name,
    p.birth_date,
    CONCAT(o.first_name, ' ', o.last_name) AS owner_full_name
FROM
    pets AS p
        LEFT JOIN
    pet_owners AS o ON p.owner_id = o.owner_id
WHERE
    o.first_name LIKE 'M%'
ORDER BY p.pet_name;

-- Display the owner’s name, owner ID, and province of residence for all pet owners who do not reside in the province of Latina. 
SELECT 
    CONCAT(o.first_name, ' ', o.last_name) AS owner_full_name,
    o.owner_id,
    c.county
FROM
    pet_owners AS o
        LEFT JOIN
    cities AS c ON c.city_id = o.city_id
WHERE
    NOT c.county = 'LT'
ORDER BY owner_full_name;

-- Display the total number of pets in each city; sort by total number of pets in descending order, and by city name in alphabetical order from A to Z.
SELECT 
    c.city_name, COUNT(p.pet_id) AS pets_tot_num
FROM
    cities AS c
        LEFT JOIN
    pet_owners AS o ON c.city_id = o.city_id
        LEFT JOIN
    pets AS p ON o.owner_id = p.owner_id
GROUP BY c.city_name
ORDER BY pets_tot_num DESC , c.city_name;

-- Display the ID, name, email address, and phone number of all pet owners living in Bassiano (SQL subqueries).
SELECT 
    owner_id,
    CONCAT(o.first_name, ' ', o.last_name) AS owner_full_name,
    email_address,
    phone_number
FROM
    pet_owners AS o
WHERE
    city_id = (SELECT 
            city_id
        FROM
            cities
        WHERE
            city_name = 'Bassiano');
 
-- Alternative without SQL subqueries:

SELECT 
    o.owner_id,
    o.first_name,
    o.last_name,
    o.email_address,
    o.phone_number
FROM
    pet_owners AS o
        JOIN
    cities AS c ON o.city_id = c.city_id
WHERE
    c.city_name = 'Bassiano';
 
-- Display the ID, name, email address, phone number, and city of residence for all pet owners living in the County of Latina: Sort by owner's name from A to Z.
SELECT 
    o.owner_id,
    CONCAT(o.first_name, ' ', o.last_name) AS owner_full_name,
    o.email_address,
    o.phone_number,
    c.city_name
FROM
    pet_owners AS o
        LEFT JOIN
    cities AS c ON o.city_id = c.city_id
WHERE
    county = 'LT'
ORDER BY owner_full_name;

-- Display each veterinarian's ID, name, years of experience (since graduation), salary, and the number of visits performed in the current year.
SELECT 
    ve.veterinarian_id,
    CONCAT(ve.first_name, ' ', ve.last_name) AS vet_full_name,
    YEAR(NOW()) - YEAR(ve.graduation_date) AS experience_years,
    ve.salary,
    COUNT(vi.visit_date) AS tot_visits_2023
FROM
    veterinarians AS ve
        LEFT JOIN
    visits AS vi ON ve.veterinarian_id = vi.veterinarian_id
WHERE
    vi.visit_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY ve.veterinarian_id , vet_full_name
ORDER BY vet_full_name;

-- For each veterinarian, display the full name and the number of visits made in the second half of the current year; sort in alphabetical order.
SELECT 
    CONCAT(ve.first_name, ' ', ve.last_name) AS vet_full_name,
    COUNT(vi.visit_date) AS tot_visits_2023
FROM
    veterinarians AS ve
        LEFT JOIN
    visits AS vi ON ve.veterinarian_id = vi.veterinarian_id
WHERE
    vi.visit_date BETWEEN '2023-06-01' AND '2023-12-31'
GROUP BY vet_full_name
ORDER BY vet_full_name;

-- Extra #1: Select top veterinarians by number of visits.
SELECT 
    ve.veterinarian_id,
    CONCAT(ve.first_name, ' ', ve.last_name) AS vet_full_name,
    COUNT(vi.visit_serial) AS total_visits
FROM
    veterinarians AS ve
        LEFT JOIN
    visits AS vi ON ve.veterinarian_id = vi.veterinarian_id
GROUP BY ve.veterinarian_id
ORDER BY total_visits DESC
LIMIT 1;

-- Extra #2: Select owners owning multiple pets.
SELECT 
    o.owner_id,
    CONCAT(o.first_name, ' ', o.last_name) AS owner_full_name,
    COUNT(p.pet_id) AS total_pets
FROM
    pet_owners AS o
        LEFT JOIN
    pets AS p ON o.owner_id = p.owner_id
GROUP BY o.owner_id
HAVING COUNT(p.pet_id) > 1
ORDER BY total_pets DESC;

-- Extra #3: Select the most common species in clinic
SELECT 
    s.species_name,
    s.common_name,
    COUNT(p.pet_id) AS occurrences
FROM
    species AS s
        JOIN
    pets AS p ON s.species_id = p.species_id
GROUP BY s.species_id
ORDER BY occurrences DESC
LIMIT 5;

/* Any feedback is welcome,
thanks for having a look at my SQL projects! */