from itertools import product
from multiprocessing import Pool
from tqdm import tqdm

with open('data/2024-07.txt', 'r') as f:
    d = f.read().split('\n')
    
# d = ['18: 1 6 2', '9: 1 2 3']

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
    f = generate_combinations(v.split(), x)
    f2 = generate_combinations(v.split(), x, ['*', '+', ''])
    return f, f2

if __name__ == "__main__":
    with Pool() as pool:
        f = tqdm(pool.imap_unordered(task, d), total=len(d))
        f1, f2 = zip(*f)
    print()
    print("Part 1: ", sum(f1))
    print("Part 2: ", sum(f2))