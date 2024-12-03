import re

with open('03.txt', 'r') as f:
    d = f.read()

print(sum((int(r[0]) * int(r[1])) for r in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", d)))

e = True
c = 0
pf = 0
for r in re.finditer(r"mul\((?P<d1>\d{1,3}),(?P<d2>\d{1,3})\)", d):
    m = re.search(r".*((?P<do>do\(\))|(?P<dont>don't\(\)))", d[pf:r.start()])
    if m and m.group('do'):
        e = True
    elif m and m.group("dont"):
        e = False

    pf = r.end()

    if e:
        c += int(r['d1']) * int(r['d2'])

print(c)