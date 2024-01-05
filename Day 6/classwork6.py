limit = 18
age = int(input("How old are you?"))
height = int(input("How tall are you?"))

if age >= limit and height >= 180:
    print("You are adult and tall enough.")
elif age < limit and height >= 180:
    print("You are tall, but not big enough.")
elif age >= limit and height < 180:
    print("You are adult, but not tall enough.")
else:
    print("You are not adult and you are not tall enough too.")

if True:
    print("1")
elif not(1+1 == 3):
    print("2")
else:
    print("3")

if True:
    print("423")

balance = 780.5
print(type(balance))

i = 1
while i <=5:
    print(i)
    i = i + 1

print("finished")

birth_year = input()
print(type(birth_year))



