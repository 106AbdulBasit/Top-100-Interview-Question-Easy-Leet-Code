import re
s = "A man, a plan, a canal: Panama"
f =re.sub(r'\W+', '', s)
g =f.lower()
print(g)
firstp = 0
lastp = len(g) - 1


while firstp < lastp:
    ch1 = g[firstp]
    ch2 = g[lastp]
    if not g[firstp].isalnum():
            firstp += 1
    elif not g[lastp].isalnum():
            lastp -= 1
    else :
        if ch1 != ch2:
            print('false')
    firstp += 1
    lastp -= 1
print(True)
   

'''g = list(g)
lst2 = g.copy()
lst2.reverse()
if g == lst2:
    print("Plaindrome")
else:
    print("not plaindrome")'''
