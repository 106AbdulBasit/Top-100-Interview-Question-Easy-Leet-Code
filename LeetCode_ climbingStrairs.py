
from itertools import combinations
def starirs(s):
     prev = 1
     cur = 1      
     for i in range(2, s+1):
         temp = prev + cur
         prev = cur
         cur = temp
     return cur


q = 6
print(starirs(q))

for i in range(2,6):
    print(i)