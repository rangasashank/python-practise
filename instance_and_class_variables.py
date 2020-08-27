class Employee:
    no_of_leaves = 30
    pass

harry = Employee()
sashi = Employee()

harry.name = "Harry"
harry.salary = 200000
harry.role = "Instructor"


sashi.name = "Sashi"
sashi.salary = 10000
sashi.role = "Student"

print(Employee.no_of_leaves)

print(sashi.__dict__)
print(sashi.no_of_leaves)
sashi.no_of_leaves = 21
print(sashi.__dict__)
print(sashi.no_of_leaves)

print(Employee.__dict__)
Employee.no_of_leaves = 38
print(Employee.__dict__)
print(Employee.no_of_leaves)
