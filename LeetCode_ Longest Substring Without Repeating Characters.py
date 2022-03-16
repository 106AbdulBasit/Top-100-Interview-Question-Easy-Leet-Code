'''
Given a string s, find the length of the 
longest substring without repeating characters.

'''
'''
s = "pwwkew"
f = set()
coun1 = 0
for i in range(len(s)):
    for j in range(i,len(s)+1):
        res = s[i:j]
        if(len(set(res)) == len(res)) and len(res) > coun1:
            coun1 = len(res)
            print(res)
print(coun1)'''

def longestSub(s):
    i = 0
    j =0
    maximum = 0
    d = set()

    while i < len(s):
        chacter1 = s[i]
        while chacter1 in d:
            d.remove(s[j])
            j +=1
        d.add(chacter1)
        maximum = max(maximum, i-j+1)
        i +=1
    return maximum

s = "abcabcbb"
print(longestSub(s))        