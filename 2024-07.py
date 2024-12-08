from itertools import product
from tqdm import tqdm

with open('data/2024-07.txt', 'r') as f:
    d = f.read().split('\n')

def generate_combinations(my_list, x, operators=['*', '+']):
    operator_combinations = product(operators, repeat=len(my_list)-1)

    for ops in operator_combinations:
        c = int(my_list[0])
        for i, op in enumerate(ops):
            c = eval(f"{str(c)}{op}{my_list[i+1]}")
        if c == x:
            return x
    return 0

def task(i):
    x, v = i.split(': ')
    x = int(x)
    f += generate_combinations(v.split(), x)
    f2 += generate_combinations(v.split(), x, ['*', '+', ''])
    return f, f2

f = 0
f2 = 0
for i in tqdm(d):
    x, v = i.split(': ')
    x = int(x)
    f += generate_combinations(v.split(), x)
    f2 += generate_combinations(v.split(), x, ['*', '+', ''])
    
print("Part 1: ", f)
print("Part 2: ", f2)