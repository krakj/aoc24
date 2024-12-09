from tqdm import tqdm

with open('data/2024-09.txt', 'r') as f:
    d = f.read()
    
files = list(map(int, d[::2]))
free = list(map(int, d[1::2]))

# Create a list of idid...idid like in the example
o = []
for i, f in enumerate(files):
    o.extend([i]*f)
    o.extend((free[i])*['.'] if not len(free) == i else [])

# get the ids in reverse order
r = [v for v in o[::-1] if v != '.']
lr = len(r)

# replace every . with the first value from the reverse ids
# finally remove values from the right side of the list for all inserted values
m = [r.pop(0) if  v == '.' else v for v in o][:-(lr-len(r))]

print("Part 1: ", sum([i*v for i, v in enumerate(m)]))

# Part 2:
# Create a dict of id: spaces taken
m = {i: f for i, f in enumerate(files)}

# Go over it in reverse
for id, v in tqdm(sorted(m.items(), reverse=True)):
    n = 0
    for i,r in enumerate(free): # for each free space
        if v <= r: # if it has enough space
            b = [oi for oi, ov in enumerate(o) if ov == '.'][n] # get the first index of the free space
            if b < o.index(id): # make sure the free space is after the original space
                o = ['.' if z == id else z for z in o] # replace the old space with dots
                o[b:b+v] = [id]*v # insert the id in the new spaces
                
                free[i] = r-v # update the list of free spaces
                try: # remove empty spaces from the list of free spaces (optional, helped with debugging)
                    free.remove(0)
                except:
                    pass
            break
        else: # update count of how many dots have been passed
            n += r
    
print("Part 2: ", sum([i*v for i, v in enumerate(o) if v != '.']))