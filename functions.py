def strings(n):
    print("Your numbers is: ", n)

#strings(5)

def sum(a,b):
    return a + b

#print(sum(4,5))

def ghost_number(n):
    return lambda f : f * n

number = ghost_number(20)

print(number(2))