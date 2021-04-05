class Instructors:
    companyName = "Blulime"

    def __init__(self,course, duration):
        self.course = course
        self.duration = duration

    def printInfo(self):
        print("My Company name is", self.companyName)

elearning = Instructors("Python for beginners", 7)

bls = Instructors("Django for beginners", 8)

elearning.printInfo()
bls.printInfo()

print(bls.course)
print(bls.duration)