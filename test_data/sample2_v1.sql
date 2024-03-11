SELECT 
  employee_id,
  last_name,
  first_name,
  salary,
  RANK() OVER (ORDER BY salary DESC) as ranking
FROM employee
ORDER BY ranking