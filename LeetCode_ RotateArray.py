'''
Given an array, rotate the array to the right by k steps, 
where k is non-negative.
'''

def Rotate_Array(s,k):
    k = k % len(s)
    print(k)
   
        #print(s)
    s= s[-k::] +  s[:-k]
                 
    return s

nums = [1,2,3,4,5,6,7] 
r = 3
print(Rotate_Array(nums,r))