def my_decorator(function):
    def wrapper():
        myFunction = function()
        convert_uppercase = myFunction.upper()
        return convert_uppercase
    return wrapper

@my_decorator
def say_hello():
    return "hello everyone"

#decorate = my_decorator(say_hello)
#print(decorate())

print(say_hello())