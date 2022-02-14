'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def multipleofarray(a,e):
    for i in a:
       f = a[1::]
       c = multiply_manual(f) #pairs multiplication
       e.append(c)
       a = a[1:] + a[:1]
    return e


def multiply_manual(iterable):
    prod = 1
    for x in iterable:
        prod *= x

    return prod


s = [1,2,3,4,5]
b = []
print(multipleofarray(s,b))
'''for i in s:
    print(i)
    print(s[1::])
    f = s[1::]
    c = multiply_manual(f)
    b.append(c)
    s = s[1:] + s[:1]
    print(s)

print(b)'''

    
