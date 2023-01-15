from typing import List
from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        st = set(nums)
        dp = Counter()
        ans = 0
        for x in nums:
            if x-1 in st:
                dp[x] = dp[x-1] + 1
            else:
                dp[x] = 1
            ans = max(ans, dp[x])
        return ans

print(Solution().longestConsecutive(nums = [100,4,200,1,3,2]))
print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))