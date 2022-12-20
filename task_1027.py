from functools import cache
from typing import List
from bisect import bisect_right

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        pz = {}
        for i, x in enumerate(nums):
            if x not in pz:
                pz[x] = []
            pz[x].append(i)

        inf = int(1e9+228)
        
        @cache
        def solve(i, d):
            next = nums[i]+d
            idx = inf if next not in pz else bisect_right(pz[next], i)
            if idx == inf or idx >= len(pz[next]):
                return 1
            return solve(pz[next][idx], d)+1
        
        ans, mxD = 0, max(nums)-min(nums)
        st = set()
        for i in range(n):
            if nums[i] in st:
                continue
            st.add(nums[i])
            
            for d in range(-mxD, mxD+1):
                ans = max(ans, solve(i, d))
                # print(f'dp[{i, d}] = {solve(i,d)}')
        
        return ans

print(Solution().longestArithSeqLength(nums=[3,6,9,12]))
print(Solution().longestArithSeqLength(nums=[9,4,7,2,10]))
print(Solution().longestArithSeqLength(nums=[20,1,15,3,10,5,8]))