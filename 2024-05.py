from collections import defaultdict

with open('data/2024-05.txt', 'r') as f:
    p, d = f.read().split('\n\n')
    
rules = defaultdict(set)
p = [(x, y) for i in p.split('\n') for x, y in [map(int, i.split('|'))]]
for x, y in p:
    rules[x].add(y)

d = [list(map(int, i.split(','))) for i in d.splitlines()]

c = 0
bad = []
for r in d:
    f = False
    for i, e in enumerate(r):
        b = set(r[:i])
        if len(b.intersection(rules[e])) > 0:
            f = True
            break
    if f:
        bad.append(r)
        continue
    c += r[int(len(r)/2)]

print("Part 1: ", c)

def reorder(r):
    for i, e in enumerate(r):
        b = set(r[:i])
        x = list(b.intersection(rules[e]))
        if len(x) > 0:
            for a in x:
                r.append(a)
                r.remove(a)
            reorder(r)
    return r

c = 0
for r in bad:
    r = reorder(r)
    c += r[int(len(r)/2)]
    
print("Part 2: ", c)