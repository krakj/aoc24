with open('data/2024-01.txt', 'r') as f:
    d = f.read()
    
l1 = []
l2 = []

for r in d.splitlines():
    x, y = filter(None, r.split(' '))
    l1.append(int(x))
    l2.append(int(y))
    
l1.sort()
l2.sort()

# Part 1
print(sum([abs(l-r) for l, r in zip(l1, l2)]))

# Part 2 initial answer
from collections import Counter

b = Counter(l1)
c = Counter(l2)

print(sum((c[k]*k*v for k, v in b.items())))