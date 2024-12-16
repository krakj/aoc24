import time
start = time.time()

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

with open('data/2024-16.txt', 'r') as f:
    d = f.read()

g = {complex(i,j): v for i, r in enumerate(d.split('\n')) for j, v in enumerate(r)}
pos = [p for p, v in g.items() if v == 'S'][0]
best_score = 10**10
all_visited = defaultdict(set)

def move(pos, dir=1j, score=0, visited={}, old_visited=set()):
    global best_score
    if score > best_score or not (v:=g.get(pos)) or v == '#' or (vi:=visited.get(pos)) and vi <= score:
        return False
    visited[pos] = score
    old_visited.add(pos)
    new_visited = old_visited.copy()
    if v == 'E':
        if score < best_score:
            best_score = score
        if score == best_score:
            all_visited[score].update(new_visited)
        return True
    
    score += 1
    move(pos+dir, dir, score, visited, new_visited)
    score += 1000
    left, right = dir*-1j, dir*1j
    move(pos+left, left, score, visited, new_visited)
    move(pos+right, right, score, visited, new_visited)
    
move(pos)
print("Part 1: ", best_score)
print("Part 2: ", len(all_visited[best_score]))
print(f"Runtime: {time.time()-start:.3f} seconds")