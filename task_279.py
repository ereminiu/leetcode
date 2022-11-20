from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        p = []
        for i in range(1, n+1):
            if i*i > n:
                break
            p.append(i*i)
        
        @cache
        def go(x):
            if x == 0:
                return 0
            
            ret = int(1e9+228)
            for y in p:
                if y > x:
                    break
                ret = min(ret, go(x-y)+1)
            return ret
        
        return go(n)

print(Solution(int(input())))