from tqdm import tqdm

with open('data/2024-12.txt', 'r') as f:
    d = f.read()

G = {(p:=complex(i,j)): {'v': v} for i,r in enumerate(d.split('\n')) for j,v in enumerate(r)}

r2m = set()
for p, v in G.items():
    regions = {p+dr for dr in (-1, 1, -1j, 1j) if (n:=G.get(p+dr)) and n['v'] == v['v']}
    G[p]['b'] = 4-(l:=len(regions))
    regions.add(p)
    r2m.add(frozenset(regions))
    
while True:
    bs = set()
    for r in tqdm(r2m):
        for v in r2m:
            if len(r.intersection(v)) > 0:
                r = r.union(v)
        bs.add(frozenset(r))
    if len(bs) == len(r2m):
        break
    r2m = bs

print("Part 1: ", sum(v['b']*len(r) for r in bs for e in r if (v:=G.get(e))))

n = 0
for x in bs:
    u = 0
    for e in x:
        if not e-1 in x:
            u += 1 if not e-1j in x else 0
            u += 1 if not e+1j in x else 0
        else:
            u += 1 if e+1j in x and e+(-1+1j) not in x else 0
            u += 1 if e-1j in x and e+(-1-1j) not in x else 0
        if not e+1 in x:
            u += 1 if not e-1j in x else 0
            u += 1 if not e+1j in x else 0
        else:
            u += 1 if e+1j in x and e+(1+1j) not in x else 0
            u += 1 if e-1j in x and e+(1-1j) not in x else 0
            
    n += u*len(x)
    
print("Part 2: ", n)