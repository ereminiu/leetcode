from typing import List
from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def go(i, x):
            if i == -1 and x == 0:
                return 1
            if i == -1:
                return 0
            
            return go(i-1, x-nums[i]) + go(i-1, x+nums[i])
        
        return go(len(nums)-1, target)

nums = list(map(int, input().split()))
target = int(input())
print(Solution().findTargetSumWays(nums, target))