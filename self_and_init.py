class Employee:
    no_of_leaves = 30

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"


harry = Employee("Harry", 255, "instructor")
sashi = Employee("Sashi", 200, "student")

# harry.name = "Harry"
# harry.salary = 200000
# harry.role = "Instructor"
#
#
# sashi.name = "Sashi"
# sashi.salary = 10000
# sashi.role = "Student"

print(harry.printdetails())
print(sashi.printdetails())