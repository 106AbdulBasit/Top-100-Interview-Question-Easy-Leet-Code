'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''

def remove_negative(b,a):
    b = list(dict.fromkeys(b))
    for x in b:
        if x > 0:
            a.append(x)
    return a


def first_positive(s):
    b = []
    min_val = 1
    s = remove_negative(s,b)
    s.sort()
    for i in range(len(s)):
        if s[i] - min_val < 1:
            min_val +=1
        elif s[i] - min_val > 1:
            min_val == 1
    return min_val

b = [-1,-3]
print(first_positive(b))





