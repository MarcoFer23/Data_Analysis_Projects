-- For this query exercise, we will use the university database from the previous exercises; here are a couple of interesting SQL queries:

-- For each student, select their id, name, highest, lowest and average grade:

SELECT 
    s.student_id,
    s.student_name,
    MAX(e.exam_grade) AS highest_grade,
    MIN(e.exam_grade) AS lowest_grade,
    AVG(e.exam_grade) AS average_grade
FROM
    students AS s
        INNER JOIN
    exams AS e ON s.student_id = e.student_id
GROUP BY s.student_id , s.student_name;

-- For each student, select their id, name, highest, lowest and average grade (with exam date between 2020/01/01 and 2022/12/31 and average grade higher than 25):

SELECT 
    s.student_id,
    s.student_name,
    MAX(e.exam_grade) AS highest_grade,
    MIN(e.exam_grade) AS lowest_grade,
    AVG(e.exam_grade) AS average_grade
FROM
    students s
        INNER JOIN
    exams e ON s.student_id = e.student_id
WHERE
    e.exam_date BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY s.student_id , s.student_name
HAVING AVG(e.exam_grade) > 25
ORDER BY average_grade DESC;