# stars in 0 to n
''' 
# list = [   0        1        2       3          4    ...n]
animals = ["bear", "tiger", "lion", "panda", "elephant"]

for animal in animals:
    print(animal)
print(animals)

print(animals[0]) # print selected item
print(animals[-1]) # starts from back 
print(animals[1:]) # list all after the item selected
print(animals[1:3]) # list all in range

animals[0] = "dog" # modify selected item

print(animals) 
'''

# List methods
fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

''' 
fruits.extend(vegetables)
print(fruits) 

vegetables.append("bean") # add item to the list
print(vegetables)

vegetables.sort() # sort ascending
print(vegetables)

vegetables.sort(reverse=True) # sort descending
print(vegetables) 

quantity = fruits.count("berries") 
print(quantity)

print(fruits.index("grapes"))

fruits.insert(0,"bannana")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("apples")
print(fruits)
'''

del vegetables
print(vegetables)