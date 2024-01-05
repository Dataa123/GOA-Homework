# name = "data diasamidze"
# print(name.split())

# name = ("dsat", "yhadg")
# index = name.find("dsat") 

# array = ["dnsfa", "needle", "sgtaga"]
# def find_needle(haystack):
#     index = haystack.index("needle")
#     return ("found the needle at position " + str(index))
# print(find_needle(array))

nums = [1, 2, 3, -4]
def sum_array(a):
    my_sum = 0
    n = 0
    if a == []:
        return 0
    while n < len(a):
        my_sum += a[n]
        n += 1
        return my_sum
print(sum_array(nums))