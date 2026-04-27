-- Select the "world" database

USE world;

-- Query example (with CASE. JOINs, WHERE and ORDER BY)

SELECT
	c.ID AS CityID,
    c.Name AS City,
    co.Name AS Country,
    c.CountryCode, 
    c.Population,
    co.Continent,
    cl.Language,
    CASE
		WHEN cl.IsOfficial = "T" THEN "Yes"
        WHEN cl.IsOfficial = "F" THEN "No"
        ELSE "N.d."
	END AS IsOfficial
FROM city AS c
JOIN country AS co ON c.CountryCode = co.Code
JOIN countrylanguage AS cl ON co.Code = cl.CountryCode
WHERE cl.IsOfficial = "T"
ORDER BY CityID;


-- Select the "sakila" database

USE sakila;

-- Query example (with JOINs and ORDER BY [containing a rule for null values as well])

SELECT
    a.actor_id,
    a.first_name,
    a.last_name,
    f.film_id,
    f.title,
    f.release_year,
    f.rating,
    l.name AS language
FROM actor AS a
JOIN film_actor AS fa ON a.actor_id = fa.actor_id
JOIN film AS f ON f.film_id = fa.film_id
JOIN language AS l ON l.language_id = f.language_id
ORDER BY f.title IS NULL, f.title;