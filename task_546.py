from typing import List
from functools import cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        def solve(l: int, r: int, k: int):
            if l > r:
                return 0
            while l < r-1 and boxes[l] == boxes[l+1]:
                l += 1; k += 1
            
            ret = (k+1)**2 + solve(l+1, r, 0)
            for i in range(l+1, r+1):
                if boxes[i] == boxes[l]:
                    ret = max(ret, solve(i, r, k+1) + solve(l+1, i-1, 0))
            
            return ret

        return solve(0, n-1, 0)

print(Solution().removeBoxes(boxes = [1,3,2,2,2,3,4,3,1]))
print(Solution().removeBoxes(boxes = [1,1,1]))
print(Solution().removeBoxes(boxes = [1]))