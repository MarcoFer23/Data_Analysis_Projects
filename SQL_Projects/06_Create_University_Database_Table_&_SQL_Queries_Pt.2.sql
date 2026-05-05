-- For this query exercise, we will use the university database from the previous exercises:

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
    exam_grade TINYINT NOT NULL CHECK (exam_grade BETWEEN 18 AND 30),
    PRIMARY KEY (exam_id),
    FOREIGN KEY (course_id)
        REFERENCES courses (course_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (student_id)
        REFERENCES students (student_id)
        ON UPDATE CASCADE ON DELETE NO ACTION,
    UNIQUE (student_id , course_id , exam_date)
);

-- Let's add some tables and alter an existing one to try more advanced SQL queries:

ALTER TABLE students
ADD COLUMN graduation_grade INT CHECK (graduation_grade BETWEEN 66 AND 110);

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL,
    scientific_area VARCHAR(255) NOT NULL,
    PRIMARY KEY (department_id)
);

CREATE TABLE master_programs (
    master_id INT AUTO_INCREMENT,
    master_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    available_slots INT NOT NULL,
    publication_date DATE NOT NULL,
    PRIMARY KEY (master_id),
    FOREIGN KEY (department_id)
        REFERENCES departments (department_id)
);

CREATE TABLE student_master_applications (
    student_id INT NOT NULL,
    master_id INT NOT NULL,
    application_date DATE NOT NULL,
    PRIMARY KEY (student_id , master_id),
    FOREIGN KEY (student_id)
        REFERENCES students (student_id),
    FOREIGN KEY (master_id)
        REFERENCES master_programs (master_id)
);

-- Find students who applied twice or more to master programs:

SELECT 
    s.student_id, s.student_name, COUNT(*) AS total_applications
FROM
    students s
        JOIN
    student_master_applications sma ON s.student_id = sma.student_id
GROUP BY s.student_id , s.student_name
HAVING COUNT(*) >= 2
ORDER BY s.student_name;

-- Find master programs having 7 or more slots:

SELECT 
    d.department_name, d.scientific_area, mp.master_name, mp.available_slots
FROM
    departments d
        JOIN
    master_programs mp ON d.department_id = mp.department_id
WHERE
    mp.available_slots >= 7;

-- Find students with graduation grade higher than 100 and at least 2 master applications:

SELECT 
    s.student_id, s.student_name
FROM
    students s
        JOIN
    student_master_applications sma ON sma.student_id = s.student_id
WHERE
    s.graduation_grade > 100
GROUP BY s.student_id , s.student_name
HAVING COUNT(sma.master_id) >= 2;