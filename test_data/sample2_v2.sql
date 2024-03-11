SELECT 
  employee_id,
  salary,
  RANK() OVER (ORDER BY salary DESC) as ranking
FROM employee
ORDER BY ranking