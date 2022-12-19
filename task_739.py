from typing import List
from bisect import bisect_right

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = n * [0]
        pz = {}
        for i, x in enumerate(temp):
            if x not in pz:
                pz[x] = []
            pz[x].append(i)
        
        for i in range(n-1):
            mn = int(1e9+228)
            for next in range(temp[i]+1, 101):
                if next not in pz:
                    continue
                ln = len(pz[next])
                idx = bisect_right(pz[next], i)
                if pz[next][ln-1] < i or idx == ln:
                    continue
                mn = min(mn, pz[next][idx]-i)
            ans[i] = 0 if mn == int(1e9+228) else mn
        
        return ans

print(Solution().dailyTemperatures(temp=[73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures(temp=[30,40,50,60]))
print(Solution().dailyTemperatures(temp=[30,60,90]))