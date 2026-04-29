/* One basic exercise to practice database table creation, and basic SQL queries.
Let's create an airport database, and fill it with dedicated tables: */

CREATE DATABASE airport_data;

USE airport_data;


CREATE TABLE airports (
    iata_code CHAR(3) NOT NULL,
    airport_name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    runways TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (iata_code),
    CONSTRAINT chk_iata_upper CHECK (iata_code = UPPER(iata_code)),
    CONSTRAINT chk_runways CHECK (runways > 0)
);

CREATE TABLE airplanes (
    airplane_id INT NOT NULL AUTO_INCREMENT,
    airplane_type VARCHAR(255) NOT NULL,
    passenger_capacity SMALLINT UNSIGNED NOT NULL,
    goods_volume INT UNSIGNED NOT NULL,
    PRIMARY KEY (airplane_id)
);

CREATE TABLE flights (
    flight_id INT NOT NULL AUTO_INCREMENT,
    airplane_id INT NOT NULL,
    departure_airport CHAR(3) NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    destination_airport CHAR(3) NOT NULL,
    landing_time TIMESTAMP NOT NULL,
    PRIMARY KEY (flight_id),
    FOREIGN KEY (airplane_id)
        REFERENCES airplanes (airplane_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (departure_airport)
        REFERENCES airports (iata_code)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (destination_airport)
        REFERENCES airports (iata_code)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE INDEX idx_route ON flights(departure_airport, destination_airport);
CREATE INDEX idx_departure_time ON flights(departure_time);
CREATE INDEX idx_landing_time ON flights(landing_time);

-- Let's search for airports with a total number of runways between 2 and 5:

SELECT iata_code, airport_name, city
FROM airports
WHERE runways BETWEEN 2 and 5;

-- Search for flights arriving at Keflavik (Reykjavik) airport:

SELECT flight_id, airplane_id, departure_airport, departure_time
FROM flights
WHERE destination_airport = 'KEF';

-- Search for flights arriving at an airport whose Iata Code starts with K:

SELECT flight_id, airplane_id, departure_airport, departure_time
FROM flights
WHERE destination_airport LIKE 'K%';

-- Search for flights taking off from Keflavik (Reykjavik) airport:

SELECT flight_id, airplane_id
FROM flights
WHERE departure_airport = 'KEF';

-- Search for flights having both departure and destination airports following specific patterns:

SELECT flight_id, airplane_id, departure_time
FROM flights
WHERE departure_airport LIKE 'J%' AND destination_airport LIKE 'K%';