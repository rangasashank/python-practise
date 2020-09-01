class Employee:
    no_of_leaves = 30

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    def __add__(self, other):
        return self.salary + other.salary
    def __repr__(self):
        return f"Employee('{self.name}', '{self.salary}', '{self.role}')"
    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

emp1 = Employee("Harry", 345, "Programmer")
emp2 = Employee("Sashi", 999, "manager")
print(emp1)