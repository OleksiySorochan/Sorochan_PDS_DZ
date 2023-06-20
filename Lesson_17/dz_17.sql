-- 1
-- SELECT COUNT(JOB_ID)  FROM employees;
-- 2
-- SELECT AVG(SALARY), COUNT(*) FROM employees WHERE DEPARTMENT_ID ='90';
-- 3
-- SELECT JOB_ID, COUNT(*) FROM employees GROUP BY JOB_ID
-- 4
-- SELECT concat( FIRST_NAME,'  ', LAST_NAME) AS NAME, DEPARTMENT_ID, FIRST_NAME FROM employees;
-- 5
 -- SELECT concat( FIRST_NAME,'  ', LAST_NAME) AS NAME,  jobs.JOB_TITLE, employees.DEPARTMENT_ID, FIRST_NAME, locations.CITY 
 -- from employees
 -- INNER JOIN jobs ON employees.JOB_ID = jobs.JOB_ID
 -- INNER JOIN departments ON employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
 -- INNER JOIN locations ON departments.LOCATION_ID = locations.LOCATION_ID
 -- WHERE CITY = 'London';
 
 