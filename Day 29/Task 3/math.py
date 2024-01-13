print("Hello this is easy calculator, created by me.")
print("There are several mathematical operations you can use:")

list = ["+", "-", "/", "*"]

print(list)
print("You also can use two numbers.")
print("So, calculator stands for writing 2 numbers and choosing mathematical operation.")

number1 = input("Choose first number: ")
math_op = input("Choose mathematical operation: ")
number2 = input("Choose second number: ")

if math_op == "+":
    print("Answer:", int(number1) + int(number2))
elif math_op == "-":
    print("Answer:", int(number1) - int(number2))
elif math_op == "/":
    print("Answer:", int(number1) / int(number2))
elif math_op == "*":
    print("Answer:", int(number1) * int(number2))
