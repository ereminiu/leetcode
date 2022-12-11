import sys

sys.stdin = open('pairs.txt', 'r')
sys.stdout = open('out.txt', 'w')

a = [list(map(int, input().split())) for x in range(75)]

for x, y in a:
    print(f'[{x}, {y}], ', end='')

# N = 75

# sys.stdin = open('pairs.txt', 'r')

# a = [list(map(int, input().split())) for x in range(N)]

# for x, c in a:
#     cnt = 0
#     for p in range(1, x+1):
#         if x % p == 0:
#             cnt += 1
#     if cnt != c:
#         print(x, f'should be {cnt}, instead of {c}')
#         assert 0

# print("OK")