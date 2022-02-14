
from typing import Counter

def duplicate(n):
    lenght = len(n)
    a = Counter(n)
    count = 0
    for i in a:
        if a[i] == 1:
            count += 1
    if lenght == count:
        return False
    return True


nums = [-1,-2,-3,-1]

print(duplicate(nums))
    
