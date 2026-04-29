/* Here's another sample exercise to practice database table creation, and SQL queries.
Let's create a record label database, and fill it with dedicated tables: */

CREATE DATABASE record_label;

USE record_label;

-- =====================
-- ALBUMS
-- =====================
CREATE TABLE albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    album_title VARCHAR(255) NOT NULL,
    release_year YEAR NOT NULL,
    price DECIMAL(6,2) NOT NULL
);

-- =====================
-- TRACKS (each track belongs to one album)
-- =====================
CREATE TABLE tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    track_title VARCHAR(255) NOT NULL,
    release_year YEAR,
    album_id INT NOT NULL,
    FOREIGN KEY (album_id)
        REFERENCES albums(album_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =====================
-- ARTISTS
-- =====================
CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL
);

-- =====================
-- SINGERS (optional separate entity)
-- =====================
CREATE TABLE singers (
    singer_id INT AUTO_INCREMENT PRIMARY KEY,
    singer_name VARCHAR(255) NOT NULL
);

-- =====================
-- ARTIST ↔ ALBUM (many-to-many)
-- =====================
CREATE TABLE artist_album (
    artist_id INT NOT NULL,
    album_id INT NOT NULL,
    PRIMARY KEY (artist_id, album_id),
    FOREIGN KEY (artist_id)
        REFERENCES artists(artist_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (album_id)
        REFERENCES albums(album_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =====================
-- ARTIST ↔ TRACK (many-to-many)
-- =====================
CREATE TABLE artist_track (
    artist_id INT NOT NULL,
    track_id INT NOT NULL,
    PRIMARY KEY (artist_id, track_id),
    FOREIGN KEY (artist_id)
        REFERENCES artists(artist_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (track_id)
        REFERENCES tracks(track_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- =====================
-- TRACK ↔ SINGER (many-to-many)
-- =====================
CREATE TABLE track_singer (
    track_id INT NOT NULL,
    singer_id INT NOT NULL,
    PRIMARY KEY (track_id, singer_id),
    FOREIGN KEY (track_id)
        REFERENCES tracks(track_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (singer_id)
        REFERENCES singers(singer_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Find artists and singers having the same name, starting in 'D':

SELECT 
    s.singer_id,
    s.singer_name,
    t.track_id,
    t.track_title
FROM singers AS s
INNER JOIN track_singer ts ON s.singer_id = ts.singer_id
INNER JOIN tracks t ON ts.track_id = t.track_id
INNER JOIN artist_track at ON t.track_id = at.track_id
INNER JOIN artists a ON at.artist_id = a.artist_id
WHERE a.artist_name = s.singer_name
  AND a.artist_name LIKE 'D%';

-- Find titles of albums having tracks whose release year is null:

SELECT DISTINCT a.album_title, t.release_year
FROM albums a
INNER JOIN tracks t ON a.album_id = t.album_id
WHERE t.release_year IS NULL;

-- Find albums whose price is above the average price and release year is between 2000 and 2003:

SELECT album_id, album_title, release_year, price
FROM albums
WHERE release_year BETWEEN 2000 AND 2003
  AND price > (
        SELECT AVG(price)
        FROM albums
        WHERE release_year BETWEEN 2000 AND 2003
  );