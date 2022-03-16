


def MaximumsumWithk(s,k):
    maximumva = float('-inf')
    currentRunningSum =0
    for i in range(len(s)):
        currentRunningSum += s[i]

        
        if (i>=k-1):
            print(i,k)
            maximumva = max(maximumva,currentRunningSum)
            print(maximumva)
            currentRunningSum -= s[i-(k-1)]
            print(currentRunningSum)

    return maximumva    

def MaximumSum(s):
    maximumValue = float('-inf')
    currentWindowSum = 0
    WindowStart = 0
    for windowend in range(len(s)):
        currentWindowSum += s[windowend]   #sum
        maximumValue = max(maximumValue,currentWindowSum)

        while (currentWindowSum < 0):
            currentWindowSum -=s[WindowStart]
            
            WindowStart += 1
    return maximumValue


    
        
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
v = 3

q = MaximumsumWithk(nums,v)

print(MaximumSum(nums))


