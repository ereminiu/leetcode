n = int(input())

a = [int(input()) for x in range(n)]

vel = n * [0]
vel[0] = a[0]
for i in range(1, n):
    vel[i] = min(vel[i-1], a[i])
print(*vel)