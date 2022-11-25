import bisect

d = {}
a = [2, 2, 3, 1, 3]
n = len(a)

for i, x in enumerate(a):
    if x not in d:
        d[x] = []
    d[x].append(i)

for i, x in enumerate(a):
    idx = bisect.bisect_left(d[x], i)
    print(f'idx = {idx}')

print(d)