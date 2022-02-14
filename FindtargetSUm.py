'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
def target_sum(A,T):
    for i in range(len(A)):
        for j in range(i +1,len(A)) :
            if A[i] + A[j] == T:
                return True
    return False



li = [10, 15, 3, 7]
k = 14

print(target_sum(li,k))