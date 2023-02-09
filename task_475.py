from typing import List
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        m = len(heaters)
        
        def check(x):
            segments = []
            for i in range(m):
                segments.append([heaters[i]-x, heaters[i]+x])
            
            i = 0
            for v in houses:
                while i < m and not (segments[i][0] <= v <= segments[i][1]):
                    i += 1
            
            return i < m

        left, right = -1, int(1e9+228)
        while right-left > 1:
            mid = (left+right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        
        return right

print(Solution().findRadius(houses = [1,2,3], heaters = [2]))
print(Solution().findRadius(houses = [1,2,3,4], heaters = [1,4]))
print(Solution().findRadius(houses = [1,5], heaters = [2]))