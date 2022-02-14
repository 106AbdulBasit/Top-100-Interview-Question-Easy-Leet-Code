def extra(s):
    count = 0
    numbers = {
        'a' : 1,'b' : 1, 'c' : 2, 'd' :2, 'e' :2, 'f'  : 3, 'g' : 3, 'h': 3, 'i' : 4,
        'j' : 4,'j' : 4, 'k' : 4, 'l' :5, 'm' :5, 'n'  : 5, 'o' : 6, 'p': 6, 'q' : 6,
        'r' : 7,'s' : 7, 't' : 7, 'u' :8, 'v' :8, 'w'  : 8, 'x' : 9, 'y': 9, 'z' : 9,
         
        }
    #values =[numbers[c] for c in s]
    #return values

    for i in range(len(s)):
        for j in range(i,len(s)+1):
            #print(s[i:j])
            length = len(s[i:j])
            values = sum([numbers[c] for c in s[i:j]])
            if values > 0 and length > 0:
                if values % length == 0:
                    count +=1 
            #print(values, length)


            
    return count

q = 'abcd'
print(extra(q))