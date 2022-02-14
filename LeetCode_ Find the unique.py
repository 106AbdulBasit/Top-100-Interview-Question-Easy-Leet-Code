
from typing import Counter


def unique(s):
    c = Counter(s)
    for i in c:
        if c[i] == 1:
            return s.index(i)
    return -1


f = "loveleetcode"
test = (unique(f))
print(test)