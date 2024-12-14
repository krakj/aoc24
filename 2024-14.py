import re
from collections import Counter
from math import prod
from tqdm import tqdm

with open('data/2024-14.txt', 'r') as f:
    d = f.read().splitlines()

tall, wide = 103, 101
hmid, vmid = wide//2, tall//2

for its in tqdm(range(0,10000)):
    c = Counter()
    pos = set()
    for e in d:
        x,y, vx, vy = map(int, re.findall(r'-?\d+', e))
        
        fx = (vx*its+x)%wide
        fy = (vy*its+y)%tall
        
        pos.add(complex(fx,fy))
        
        if its == 100:
            if fx < hmid:
                if fy < vmid:
                    c['q1'] += 1
                elif fy > vmid:
                    c['q2'] += 1
            elif fx > hmid:
                if fy < vmid:
                    c['q3'] += 1
                elif fy > vmid:
                    c['q4'] += 1
        
    if its == 100:
        print("\nPart 1: ", prod(c.values()))
    z = [['.']*wide for i in range(tall)]
    for p in pos:
        z[int(p.imag)][int(p.real)] = '#'
            
    z = '\n'.join([''.join(r) for r in z])
    if '########' in z:
        print(f"\nPart 2: {its}")
        print(z)