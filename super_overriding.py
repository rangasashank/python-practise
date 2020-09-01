class A:
    classvar1 = "i am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A constructor"
        self.classvar1 = "instance var in class A"
        self.special = "special"

class B(A):
    classvar1 = "i am in class B"

    def __init__(self):

        self.var1 = "i am inside class B constructor"
        self.classvar1 = "instance var in class B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()
print(b.special, b.var1)