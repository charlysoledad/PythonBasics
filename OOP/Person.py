class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName,self.lastName)

florist = Person("Lucia", "Adams")
florist.printName()

class Lawyers(Person):
    def __init__(self,firstName, lastName, caseType):
        Person.__init__(self, firstName, lastName)
        self.caseType = caseType
    
    def printInfo(self):
        print("The case is", self.caseType)

lawyer = Lawyers("Ricardo","Aviedo", "Divorce")
lawyer.printName()
lawyer.printInfo()