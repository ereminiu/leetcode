n, m = map(int, input().split())

a = [x for x in range(m)]

def f(i):
    return (min(abs((m)//2 - i - 1), abs((m+1)//2 - i - 1)), i)

# for i in a:
#     print(i, f(i))

a.sort(key=f)

for i in range(n):
    print(a[i % m] + 1)