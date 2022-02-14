from typing import Counter


nums = [1,1,2]
q = Counter(nums)
print(q)
c = 0
for i in q:
    if q[i] > 1 or q[i] == 1:
        nums += q[i]
print(nums)
