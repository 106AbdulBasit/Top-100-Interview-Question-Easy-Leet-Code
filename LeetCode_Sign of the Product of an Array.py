nums = [-1,-2,-3,-4,3,2,1]
product = 1
for x in nums:
    product = x * product
    if (product > 1):
        print(1)
    elif (product < 0):
        print(1)
    else:
        print(0)
print(product)
