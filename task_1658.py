from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        pref, suff = n * [0], n * [0]
        pref[0], suff[n-1] = nums[0], nums[n-1]
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] + nums[i]
        inf = int(1e9+228)
        ans = inf if (bisect_left(pref, x) == n or pref[bisect_left(pref, x)] > x) else bisect_left(pref, x)+1
        for i in range(n-1, -1, -1):
            idx = bisect_left(pref, x-suff[i])
            if x-suff[i] == 0:
                ans = min(ans, n-i)
            elif idx != n and pref[idx] == x-suff[i]:
                ans = min(ans, n-i+idx+1)
        return -1 if ans == inf else ans

print(Solution().minOperations(nums = [1,1,4,2,3], x = 5))
print(Solution().minOperations(nums = [5,6,7,8,9], x = 4))
print(Solution().minOperations(nums = [3,2,20,1,1,3], x = 10))