from typing import List
from functools import cache

class Solution:
    def minSwap(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        inf = int(1e9+228)

        @cache
        def solve(i, k):
            if i == 0 and k == 0:
                return 0
            if i == 0 and k == 1:
                return 1
            
            ret = inf
            if a[i] > a[i-1] and b[i] > b[i-1]:
                ret = min(ret, solve(i-1, k) + k)
            if a[i] > b[i-1] and b[i] > a[i-1]:
                ret = min(ret, solve(i-1, k^1) + k)
            
            return ret
        
        return min(solve(n-1, 0), solve(n-1, 1))

print(Solution().minSwap(a=[0,7,8,10,10,11,12,13,19,18], b=[4,4,5,7,11,14,15,16,17,20]))
print(Solution().minSwap(a = [1,3,5,4], b = [1,2,3,7]))
print(Solution().minSwap(a = [0,3,5,8,9], b = [2,1,4,6,9]))
print(Solution().minSwap(a = [2, 2], b = [1, 3]))