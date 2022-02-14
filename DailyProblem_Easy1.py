'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
def binarySearch(A,N,T):
    l = 0
    r = N-1
    while  l <= r:
        m = ((l + r)//2)
        
        if A[m] < T:
            l  = m +1
        elif A[m] > T:
            r = m-1
        else :
            return m
    return False
    

K = [10, 15, 3, 7]
lenght = len(K)
target = 8

print(binarySearch(K,lenght,target))