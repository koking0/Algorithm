select c.Name as Employee from
    (select a.Id as Id, a.Name as Name, a.Salary as Salary, b.Salary as ManagerSalary from Employee a left join Employee b on a.ManagerId = b.Id) c
    where c.Salary > c.ManagerSalary;