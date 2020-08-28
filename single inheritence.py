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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lang = languages



    def printprog(self):
        return f"The programmer name is {self.name}. Salary is {self.salary}. Role is {self.role}. The languages are {self.lang}"


harry = Employee("Harry", 255, "instructor")
sashi = Employee("Sashi", 200, "student")
shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 655, "Programmer", ["python"])
print(karan.printprog())


