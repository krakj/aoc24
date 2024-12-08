with open('data/2024-08.txt', 'r') as f:
    d = f.read()

G = {complex(i,j): c for i, r in enumerate(d.split('\n')) for j, c in enumerate(r)}
m = set()
o = set()
for x, v in G.items():
    if v != '.':
        for y, z in G.items():
            if v == z and x != y:
                m.add(y-(x-y)) if G.get(y-(x-y)) else None
                r = 1
                while G.get(y-(x-y)*r):
                    print(x, y, y-(x-y)*r)
                    o.add(y-(x-y)*r)
                    r+=1
                o.add(x)
                
print("Part 1: ", len(m))
print("Part 2: ", len(o))