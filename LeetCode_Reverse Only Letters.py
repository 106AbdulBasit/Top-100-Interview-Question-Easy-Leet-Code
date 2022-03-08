s = "a-bC-dEf-ghIj"
s = list(s)
#print(s)
b = []
lastindex = len(s) -1
firstIndex = 0
#print(s[lastindex])
while firstIndex < lastindex:
    if not s[firstIndex].isalpha():
        firstIndex +=1
    
        continue

    if  not s[lastindex].isalpha():
        lastindex -= 1
        continue

    print(s[lastindex], s[firstIndex])
    s[lastindex] , s[firstIndex] = s[firstIndex], s[lastindex]
    print(s[lastindex], s[firstIndex], 'after chnging')
    firstIndex += 1
    lastindex -= 1


   


