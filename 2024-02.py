def good(l: list, e: bool=False) -> int:
    for i, v in enumerate(l):
        v = int(v)
        if i == 0:
            p = v
            continue
        if i == 1:
            a = True if v > p else False                
        
        if not ((a and 0 < v-p <= 3) or (not a and 0 < p-v <= 3)):
            # Alles in deze conditie is voor part 2
            if not e:
                nl = l.copy()
                nl.pop(i)
                win = good(nl, e=True)
                if win == 0:
                    ol = l.copy()
                    ol.pop(i-1)
                    win = good(ol, e=True)
                    
                    if win == 0:
                        fl = l.copy()
                        fl.pop(i-2)
                        win = good(fl, e=True)
            else:
                win = 0
            break
        
        win = 1 if i+1 == len(l) else 0
        p = v
    return win

part1 = 0
part2 = 0

with open('data/2024-02.txt', 'r') as f:
    for l in f:
        part1 += good(l.split(), e=True)
        part2 += good(l.split())

print(part1, part2)