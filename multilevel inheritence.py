class Dad:
    basketball = 1


class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes i can dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Yes i can dance{self.dance} no of yooo times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)
print(harry.isdance())

