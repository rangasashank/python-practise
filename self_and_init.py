class Employee:
    no_of_leaves = 30
    
    def printdeails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"


harry = Employee()
sashi = Employee()

harry.name = "Harry"
harry.salary = 200000
harry.role = "Instructor"


sashi.name = "Sashi"
sashi.salary = 10000
sashi.role = "Student"

print(sashi.printdeails())