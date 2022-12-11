s = input()

pz_ver = [[1, 1], [3, 1]]
pz_hor = [[1, 3], [2, 3], [3, 3], [4, 3]]

ver, hor = 0, 0
for c in s:
    if c == '0':
        print(*pz_ver[ver])
    else:
        print(*pz_hor[hor])
    ver += (c == '0'); ver %= 2
    hor += (c == '1'); hor %= 4