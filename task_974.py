from typing import List
from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = k * [0]
        mod[0] = 1
        ans, pref = 0, 0
        for i in range(n):
            pref = (pref + nums[i]) % k
            ans += mod[pref]
            mod[pref] += 1
        
        return ans

print(Solution().subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
print(Solution().subarraysDivByK(nums = [5], k = 9))
print(Solution().subarraysDivByK(nums = [8,9,7,8,9], k = 8))