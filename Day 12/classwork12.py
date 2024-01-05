# def greet(): 
#   print("Hello from a function")
#   print("Have a great day")
#   greet()


# def personal_greet(name): 
#   print("Hello", name)
#   print("Have a great day")

# personal_greet('data')


# def double(number):
#     print(number*2)
# double(2)


# def double(number):
#     print(number*2)
# double(6)


# def bmi(weight, height):
#     index = weight / (height * height)
#     return index


def bmi(weight, height):
    index = weight / (height * height)
    return index
p6 = bmi(79, 1.73)
print(p6 < 18.5)