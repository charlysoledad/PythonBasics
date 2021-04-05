def addNumbers(a,b,c=1):
    return a + b + c

#print(addNumbers(4,5,0))

class UK():
    def capitalCity(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language")

class Spain():
    def capitalCity(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language")


queen = UK()
#queen.capitalCity()

king = Spain()
#king.capitalCity()

def europe(eu):
    eu.capitalCity()

europe(queen)
europe(king)

'''
for country in (queen,king):
    country.capitalCity()
    country.language()
'''