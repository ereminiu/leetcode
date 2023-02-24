from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        inf = int(1e9+228)
        h = []

        mn = inf
        for i in range(n):
            if nums[i] % 2:
                nums[i] *= 2
            
            heapq.heappush(h, -nums[i])
            mn = min(mn, nums[i])

        ans = inf
        while h:
            mx = -heapq.heappop(h)
            ans = min(ans, abs(mx - mn))

            if mx % 2: 
                break

            heapq.heappush(h, -mx//2)
            mn = min(mn, mx//2)
        
        return ans

print(Solution().minimumDeviation(nums = [1,2,3,4]))
print(Solution().minimumDeviation(nums = [4,1,5,20,3]))
print(Solution().minimumDeviation(nums = [2,10,8]))
