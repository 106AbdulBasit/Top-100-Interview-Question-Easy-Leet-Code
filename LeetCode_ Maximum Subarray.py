def Maximumsum(s):
    count = 0
    finalresult = 0
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            subarry = s[i:j]
            result = sum(subarry)
            if result > count:
                count = result
    return count

nums = [-2,1,-3,4,-1,2,1,-5,4]

q = Maximumsum(nums)

print(q)


