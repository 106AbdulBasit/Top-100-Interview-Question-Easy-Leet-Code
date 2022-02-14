def intersection(lst1, lst2):
    ans =[]
    for value in lst1:
        if value in lst2:
            lst2.remove(value)
            ans.append(value)
    return ans

 
# Driver Code
lst1 = [1,2,2,1]
lst2 = [2]
print(intersection(lst1, lst2))