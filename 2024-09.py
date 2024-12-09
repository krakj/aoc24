from tqdm import tqdm

with open('data/2024-09.txt', 'r') as f:
    d = f.read()
    
files = list(map(int, d[::2]))
free = list(map(int, d[1::2]))

o = []
for i, f in enumerate(files):
    o.extend([i]*f)
    o.extend((free[i])*['.'] if not len(free) == i else [])

r = [v for v in o[::-1] if v != '.']
lr = len(r)

m = [r.pop(0) if  v == '.' else v for v in o][:-(lr-len(r))]

print("Part 1: ", sum([i*v for i, v in enumerate(m)])) # 6241633730082

# Part 2:
m = {i: f for i, f in enumerate(files)}

for id, v in tqdm(sorted(m.items(), reverse=True)):
    n = 0
    for i,r in enumerate(free):
        if v <= r:
            b = [oi for oi, ov in enumerate(o) if ov == '.'][n]
            if b < o.index(id):
                o = ['.' if z == id else z for z in o]
                o[b:b+v] = [id]*v
                
                free[i] = r-v
                try:
                    free.remove(0)
                except:
                    pass
            break
        else:
            n += r
    
print("Part 2: ", sum([i*v for i, v in enumerate(o) if v != '.']))