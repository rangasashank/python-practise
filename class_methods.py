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



harry = Employee("Harry", 255, "instructor")
sashi = Employee("Sashi", 200, "student")

sashi.change_leaves(35)
print(harry.no_of_leaves)