with open('data/2024-08.txt', 'r') as f:
    d = f.read()

# Create a dict with key representing the location on the map, and the value representing the field content
G = {complex(i,j): c for i, r in enumerate(d.split('\n')) for j, c in enumerate(r)}
m = set()
o = set()
for x, v in G.items():
    if v != '.':
        for y, z in G.items():
            if v == z and x != y:
                # (x-y) gives the 'step size' to from x to y
                # y-stepsize then moves that step away from y
                # G.get tests if the location f is on the grid
                f = y-(x-y)
                m.add(f) if G.get(f) else None
                r = 1
                while G.get(f):
                    o.add(f)
                    r+=1
                    f = y-(x-y)*r
                # finally add the position of x itself
                # (note that this happens inside the second loop to ensure the value isn't the only one of its kind)
                o.add(x)
                
print("Part 1: ", len(m))
print("Part 2: ", len(o))