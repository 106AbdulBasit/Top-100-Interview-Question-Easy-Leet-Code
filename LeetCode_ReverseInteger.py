x = 321
temp = x
print(temp)
if x > 0:
    x == x
    print(x)
elif x < 0:
    x = abs(x)
x = str(x)
lst = list(x) 
lst.reverse()
x = "".join(lst)
x = int(x)
#print(x)
if abs(x) < 2**31 and x != 2**31 - 1:
   x ==x
else:
   print(False)


if temp > 0:

    print(x)
elif temp < 0:
    print(-x)

#3lines of code
''''
   s = str(abs(x))
            
        reversed = int(s[::-1])
        
        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)
   '''

    