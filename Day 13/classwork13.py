def summation(num):
    my_sum = 0
    for i in range(1, num + 1):
        if num > 0:
            my_sum += i
    return my_sum
print(summation(5))