/* Here's another sample exercise to practice database table creation, data insertion and advanced SQL queries.
Let's create a sample hr company database, and fill it with dedicated tables: */

CREATE DATABASE company_employees;

USE company_employees;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (department_id)
);

CREATE TABLE roles (
    role_id INT AUTO_INCREMENT,
    role_title VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (role_id)
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT NOT NULL,
    role_id INT NOT NULL,
    manager_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (employee_id),
    FOREIGN KEY (department_id)
        REFERENCES departments (department_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (role_id)
        REFERENCES roles (role_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (manager_id)
        REFERENCES employees (employee_id)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE salary_history (
    salary_update_id INT AUTO_INCREMENT,
    employee_id INT NOT NULL,
    salary DECIMAL(10 , 2 ) NOT NULL CHECK (salary >= 0),
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (salary_update_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees (employee_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CHECK (end_date IS NULL
        OR end_date >= start_date)
);

CREATE TABLE project_statuses (
    pr_status_id INT AUTO_INCREMENT,
    pr_status VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (pr_status_id)
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT,
    project_name VARCHAR(255) NOT NULL UNIQUE,
    status_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    budget DECIMAL(12 , 2 ) NOT NULL CHECK (budget >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id),
    FOREIGN KEY (status_id)
        REFERENCES project_statuses (pr_status_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CHECK (end_date IS NULL
        OR end_date >= start_date)
);

CREATE TABLE project_roles (
    project_role_id INT AUTO_INCREMENT,
    role_name VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (project_role_id)
);

CREATE TABLE employee_projects (
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    project_role_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (employee_id , project_id , start_date),
    FOREIGN KEY (employee_id)
        REFERENCES employees (employee_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (project_id)
        REFERENCES projects (project_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (project_role_id)
        REFERENCES project_roles (project_role_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CHECK (end_date IS NULL
        OR end_date >= start_date)
);



-- After creating tables, let's fill them with sample data

INSERT INTO departments (department_id, department_name)
VALUES
(1, 'Engineering'),
(2, 'Human Resources'),
(3, 'Marketing'),
(4, 'Finance'),
(5, 'Sales');

INSERT INTO roles (role_id, role_title)
VALUES
(1, 'Software Engineer'),
(2, 'Senior Software Engineer'),
(3, 'HR Specialist'),
(4, 'Marketing Manager'),
(5, 'Accountant');

INSERT INTO employees (employee_id, first_name, last_name, email, phone, hire_date, department_id, role_id, manager_id)
VALUES
(1, 'Alice', 'Rossi', 'alice.rossi@company.com', '+39 3201111111', '2020-01-10', 1, 2, NULL),
(2, 'Marco', 'Bianchi', 'marco.bianchi@company.com', '+39 3202222222', '2021-03-15', 1, 1, 1),
(3, 'Giulia', 'Verdi', 'giulia.verdi@company.com', '+39 3203333333', '2022-06-01', 3, 4, 1),
(4, 'Luca', 'Ferrari', 'luca.ferrari@company.com', '+39 3204444444', '2019-09-20', 4, 5, NULL),
(5, 'Sara', 'Conti', 'sara.conti@company.com', '+39 3205555555', '2023-02-01', 5, 1, 2);

INSERT INTO salary_history (salary_update_id, employee_id, salary, start_date, end_date)
VALUES
(1, 1, 80000.00, '2020-01-10', NULL),
(2, 2, 55000.00, '2021-03-15', NULL),
(3, 3, 60000.00, '2022-06-01', NULL),
(4, 4, 75000.00, '2019-09-20', NULL),
(5, 5, 50000.00, '2023-02-01', NULL);

INSERT INTO project_statuses (pr_status_id, pr_status)
VALUES
(1, 'planned'),
(2, 'active'),
(3, 'completed'),
(4, 'cancelled'),
(5, 'on-hold');

INSERT INTO projects (project_id, project_name, status_id, start_date, end_date, budget)
VALUES
(1, 'Website Redesign', 2, '2024-01-10', NULL, 50000.00),
(2, 'HR System Upgrade', 1, '2024-06-01', NULL, 30000.00),
(3, 'Marketing Campaign Q2', 3, '2023-03-01', '2023-06-30', 20000.00),
(4, 'Financial Audit 2024', 2, '2024-02-01', NULL, 15000.00),
(5, 'Sales Expansion Project', 1, '2024-07-01', NULL, 40000.00);

INSERT INTO project_roles (project_role_id, role_name)
VALUES
(1, 'Frontend Developer'),
(2, 'Backend Developer'),
(3, 'Project Manager'),
(4, 'QA Engineer'),
(5, 'Business Analyst');

INSERT INTO employee_projects (employee_id, project_id, project_role_id, start_date, end_date)
VALUES
(2, 1, 1, '2024-01-10', NULL),
(3, 2, 5, '2024-06-01', NULL),
(5, 5, 2, '2024-07-01', NULL),
(2, 3, 4, '2023-03-01', '2023-06-30'),
(4, 4, 3, '2024-02-01', NULL);

-- Following are some medium-advanced SQL query samples:

-- Select employees with their department and role

SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
    d.department_name,
    r.role_title
FROM
    employees AS e
        LEFT JOIN
    departments AS d ON e.department_id = d.department_id
        LEFT JOIN
    roles AS r ON e.role_id = r.role_id
ORDER BY full_name;

-- Select employees and their manager's name

SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM
    employees AS e
        LEFT JOIN
    employees AS m ON e.manager_id = m.employee_id
ORDER BY employee_name;

-- Select projects and their respective status

SELECT 
    p.project_id, p.project_name, ps.pr_status AS project_status
FROM
    projects AS p
        JOIN
    project_statuses AS ps ON p.status_id = ps.pr_status_id
ORDER BY p.project_name;

-- Count the number of employees per department

SELECT 
    d.department_name, COUNT(e.employee_id) AS total_employees
FROM
    departments AS d
        LEFT JOIN
    employees AS e ON e.department_id = d.department_id
GROUP BY d.department_name;

-- Find an 'active' employee's latest salary

SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    ROUND(sh.salary) AS salary
FROM
    employees AS e
        LEFT JOIN
    salary_history AS sh ON e.employee_id = sh.employee_id
WHERE
    sh.end_date IS NULL
ORDER BY employee_name;

-- Select employees assigned to terminated projects with their respective role

SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    p.project_name,
    pr.role_name,
    ep.start_date,
    ep.end_date
FROM
    employee_projects AS ep
        JOIN
    employees AS e ON ep.employee_id = e.employee_id
        JOIN
    projects AS p ON ep.project_id = p.project_id
        JOIN
    project_roles AS pr ON ep.project_role_id = pr.project_role_id
WHERE
    ep.end_date IS NOT NULL
ORDER BY e.last_name;

-- Find the amount of currently active projects with the number of assigned employees

SELECT 
    p.project_name, COUNT(ep.employee_id) AS team_size
FROM
    projects AS p
        LEFT JOIN
    employee_projects AS ep ON p.project_id = ep.project_id
WHERE
    ep.end_date IS NULL
GROUP BY p.project_name
ORDER BY p.project_name;

-- Select average salary per department

SELECT 
    d.department_name, ROUND(AVG(sh.salary)) AS avg_salary
FROM
    departments AS d
        JOIN
    employees AS e ON d.department_id = e.department_id
        JOIN
    salary_history AS sh ON sh.employee_id = e.employee_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- Select employees with above-average salaries

SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    ROUND(sh.salary) AS current_salary
FROM
    employees AS e
        LEFT JOIN
    salary_history AS sh ON e.employee_id = sh.employee_id
WHERE
    sh.salary > (SELECT AVG(salary) AS avg_sal FROM salary_history); -- Subquery in WHERE statement

-- Window functions: Rank employees by current salary within department

WITH current_salary AS (
    SELECT employee_id, salary
    FROM salary_history
    WHERE end_date IS NULL
)

SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    d.department_name,
    cs.salary,
    RANK() OVER (
        PARTITION BY e.department_id
        ORDER BY cs.salary DESC
    ) AS salary_rank
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
JOIN current_salary AS cs ON e.employee_id = cs.employee_id;

-- Rank employees by hire date within each department and return the top 3 earliest hires

WITH ranked_employees AS (
    SELECT 
        e.employee_id,
        CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
        e.department_id,
        d.department_name,
        e.hire_date,
        ROW_NUMBER() OVER (
            PARTITION BY e.department_id 
            ORDER BY e.hire_date ASC, e.employee_id ASC
        ) AS row_num
    FROM employees AS e
    JOIN departments AS d 
        ON e.department_id = d.department_id
)

SELECT 
    employee_id,
    employee_name,
    department_name,
    hire_date
FROM ranked_employees
WHERE row_num <= 3;

-- Any feedback is welcome, thanks for having a look at my SQL codes!