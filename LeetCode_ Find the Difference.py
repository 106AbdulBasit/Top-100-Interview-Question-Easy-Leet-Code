from re import S


s = "a"
t = "aa"
#s = list(s)
#t = list(t)
#print(t,s)
#li_dif = [i for i in s + t if i not in t]
#q = ''.join(li_dif)
#print(q)
t = list(t)
for i in s:
    if i in t:
        t.remove(i)
print(t)