/* Here's another sample exercise to practice database table creation, and SQL queries.
Let's create a university-related database, and fill it with dedicated tables: */

CREATE DATABASE university_db;

USE university_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    student_name VARCHAR(255) NOT NULL,
    place_of_residence VARCHAR(255) NOT NULL,
    PRIMARY KEY (student_id)
);

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT,
    professor_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (professor_id)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    professor_id INT NOT NULL,
    university_department VARCHAR(255),
    PRIMARY KEY (course_id),
    FOREIGN KEY (professor_id)
        REFERENCES professors (professor_id)
        ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE exams (
    exam_id INT AUTO_INCREMENT,
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    exam_date DATE NOT NULL,
    exam_grade TINYINT UNSIGNED NOT NULL CHECK (exam_grade BETWEEN 18 AND 30),
    PRIMARY KEY (exam_id),
    FOREIGN KEY (course_id)
        REFERENCES courses (course_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (student_id)
        REFERENCES students (student_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
	UNIQUE (student_id, course_id, exam_date) -- Added this constraint to prevent duplicate exam entries. Otherwise, a student could have multiple identical exam records.
);

-- Find students whose exam grades are higher than 28:

SELECT 
    s.student_id,
    s.student_name,
    c.course_name,
    e.exam_date,
    e.exam_grade,
    p.professor_name
FROM
    students AS s
        INNER JOIN
    exams AS e ON s.student_id = e.student_id
        INNER JOIN
    courses AS c ON e.course_id = c.course_id
        INNER JOIN
    professors AS p ON c.professor_id = p.professor_id
WHERE
    e.exam_grade > 28;

-- Find professors holding exams between 2020/01/01 and 2022/12/31:

SELECT 
    p.professor_id,
    p.professor_name,
    c.course_name,
    c.university_department,
    e.exam_date
FROM
    professors AS p
        INNER JOIN
    courses AS c ON p.professor_id = c.professor_id
        INNER JOIN
    exams AS e ON c.course_id = e.course_id
WHERE
    e.exam_date BETWEEN '2020-01-01' AND '2022-12-31';