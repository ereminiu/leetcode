from typing import List
from collections import Counter

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suff = [set() for x in range(26)]
        for w in ideas:
            suff[ord(w[0]) - ord('a')].add(w[1:])
        
        ans = 0
        for i in range(26):
            for j in range(i+1, 26):
                same = len(suff[i] & suff[j])

                ans += (len(suff[i]) - same) * (len(suff[j]) - same)
        
        return 2 * ans

print(Solution().distinctNames(ideas = ["coffee","donuts","time","toffee"]))
print(Solution().distinctNames(ideas = ["lack","back"]))