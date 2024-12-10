with open('data/2024-10.txt', 'r') as f:
    G = {complex(i, j): int(w) for i, v in enumerate(f.read().split('\n')) for j, w in enumerate(v)}

n, m = 0, 0

for p in [[k] for k, v in G.items() if v == 0]:
    for i in range(0,9):
        p = [pos+d for pos in p for d in [-1, +1, 1j, -1j] if G.get(pos+d) == i+1]
        if i == 8:
            n += len(set(p))
            m += len(p)

print("Part 1: ", n, "\nPart 2: ", m)