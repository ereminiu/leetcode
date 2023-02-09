from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, a: List[List[int]]) -> int:
        pn = len(a)
        pref = [[[]] for y in range(pn)]

        Pa, MODa, Pb, MODb = 37, int(1e9+7), 39, int(1e9+9)
        mxlen = 0

        for i in range(pn):
            pm = len(a[i])
            pref[i] = [[0, 0]] * pm
            pref[i][0] = [a[i][0]+1, a[i][0]+1]
            for j in range(1, pm):
                pref[i][j][0] = (pref[i][j-1][0] * Pa + a[i][j] + 1) % MODa
                pref[i][j][1] = (pref[i][j-1][1] * Pb + a[i][j] + 1) % MODb
            
            mxlen = max(mxlen, pm+1)
        
        print(*pref, sep='\n')
        
        deg_a, deg_b = mxlen * [0], mxlen * [0]
        deg_a[0], deg_b[0] = 1, 1
        for i in range(1, mxlen):
            deg_a[i] = (deg_a[i-1] * Pa) % MODa
            deg_b[i] = (deg_b[i-1] * Pb) % MODb

        def get_sum(i, l, r):
            ret = [pref[i][r][0], pref[i][r][1]]
            if l == 0:
                return ret
            
            ret[0] = (ret[0] - (pref[i][l-1][0] * deg_a[r-l+1]) % MODa) % MODa
            ret[1] = (ret[1] - (pref[i][l-1][1] * deg_b[r-l+1]) % MODb) % MODb

            return ret
        
        def check(x, ln):
            for i in range(pn):
                fl = False
                for j in range(len(a[i])-ln+1):
                    if get_sum(i, j, j+ln-1) == x:
                        fl = True
                        break
                
                if not fl:
                    return False
            
            return True
        
        x = 4260
        y = 4260 * deg_a[3]
        print(y % MODa)
        
        print(get_sum(1, 0, 1))
        print(get_sum(0, 2, 3))
        print(get_sum(2, 3, 4))

        ans = 0
        for i in range(len(a[0])):
            left, right = i, len(a[0])
            while right-left > 1:
                mid = (left+right) // 2
                target = get_sum(0, i, mid)
                if check(target, mid-i+1):
                    left = mid
                else:
                    right = mid
            
            if check(get_sum(0, i, left), right-i):
                ans = max(ans, right-i)
        
        return ans

print(Solution().longestCommonSubpath(n = 5, a = [[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]))
# print(Solution().longestCommonSubpath(n = 3, a = [[0],[1],[2]]))
# print(Solution().longestCommonSubpath(n = 5, a = [[0,1,2,3,4],[4,3,2,1,0]]))