with open('data/2024-10.txt', 'r') as f:
    G = {complex(i, j): int(w) for i, v in enumerate(f.read().split('\n')) for j, w in enumerate(v)}
    
def move(pos, val):
    return [pos+d for d in [-1, +1, 1j, -1j] if G.get(pos+d) == val+1]
        
n = 0
m = 0
for k, v in G.items():
    if v == 0:
        p = [k]
        for i in range(0,9):
            o = []
            for b in p:
                o.extend(move(b, i))
            p = o
            if not p:
                break
            if i == 8:
                n += len(set(p))   
                m += len(p)             
print("Part 1: ", n)
print("Part 2: ", m)