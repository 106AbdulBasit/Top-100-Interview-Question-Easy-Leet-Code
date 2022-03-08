'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

'''
def power(a,b):
    
     def binaryExp(a,n):
        res = 1
        while(n):
            if n&1:
                res = res*a
                a = a*a
                n>>=1
            return res
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            x = 1/x
            n = abs(n)
    
        return binaryExp(x,n)
    


number =  2.0000
p = 10

print(power(number,p))
