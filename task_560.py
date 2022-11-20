from collections import Counter
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = n * [0]
        pref[0] = nums[0]
        counter = Counter()
        counter[nums[0]] = 1
        counter[0] += 1
        ans = 0
        
        if pref[0] == k:
            ans += 1
        
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
            ans += counter[pref[i]-k]
            counter[pref[i]] += 1
        
        return ans

nums = list(map(int, input().split()))
k = int(input())
print(Solution().subarraySum(nums, k))