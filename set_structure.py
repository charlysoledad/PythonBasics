fruits = {"grapes", "apples", "berries"}
for fruit in fruits:
    print(fruit)
print("")
animals = set(("lion", "tiger", "bear"))
for animal in animals:
    print(animal)

'''
-> Methods
add() - adds an element to a set
update() - adds multiple elements to a set
clear() - removes all elements in a set
discard() - removes a specified element or item
remove() removes a specified item from the set
del() deletes the set
'''

fruits.add("oranges")
print(fruits )

animals.update(["cobra", "horse"])
print(animals)

fruits.clear()
print(fruits)

animals.discard("tiger")
print(animals)

animals.remove("lion")
print(animals)

del fruits
print(fruits)