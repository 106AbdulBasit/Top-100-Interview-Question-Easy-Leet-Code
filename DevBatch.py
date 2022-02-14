'''a = [1,2,[3,[4,[5,[6,[],[7]]]]],8]
Required output
a= [1,2,3,4,5,6,7,8]'''
'''a = [1,2,[3,[4,[5,[6,[],[7]]]]],8]
for elemnts in a:
    if chr('[') in elemnts and ']' in elemnts:
        b = a.remove()
        print(b)'''
'''Each number on the telephone dial (except 0 and 1) corresponds to three
 alphabetic characters. Those correspondences are:
 2 ABC
 3 DEF
 4 GHI
 5 JKL
 6 MNO
 7 PRS
 8 TUV
 9 WXY
0312 1234567
print all possible "words" that your phone number (without the area code)
spells. (They may not be real english words, but just some sequence of
characters). Since the digits 0 and 1 have no alphabetic equivalent, an
input number which contains those digits should be rejected. The input will
be one or more seven digit integers from standard input.'''
'''def wordprint(s)

words = ''
for elements in s:
    if '2' in elements:
        print("ABC")
    elif '3' in elements:
        print("DEF")
    elif '4' in elements:
        print("GHI")
    elif '5' in elements:
        print("JKL")
    elif '6' in elements:
        print("MNO")
    elif '7' in elements:
        print("PRS")
    elif '8' in elements:
        print("TUV")
    elif '9' in elements:
        print("WXYZ")'''
''''a = [1,2,[3,[4,[5,[6,[],[7]]]]],8]
res = list(map(str.strip, a))
  
# Printing result
print("List after removal of special characters : " + str(res))'''
import collections
s = "helloworld"
print(collections.Counter(s).most_common(1)[0])






