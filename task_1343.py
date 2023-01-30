from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        pref = 0
        ans = 0

        for i in range(n):
            pref += arr[i]
            if i >= k:
                pref -= arr[i-k]
            
            if i >= k-1 and pref >= k * threshold:
                ans += 1
        
        return ans

print(Solution().numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(Solution().numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))