SELECT 
  employee_id,
  RANK() OVER (ORDER BY salary DESC) as ranking
FROM employee
ORDER BY ranking