from typing import List
from collections import Counter

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def more(s, t):
            ns, nt = len(s), len(t)
            equal = True
            for i in range(min(ns, nt)):
                if idx[s[i]] > idx[t[i]]:
                    return True
                elif idx[s[i]] < idx[t[i]]:
                    return False

            return ns >= nt

        idx = Counter()
        for i, c in enumerate(order):
            idx[c] = i
        
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                # print(f'{words[i], words[j], more(words[i], words[j])}')
                if more(words[i], words[j]):
                    return False
        
        return True

print(Solution().isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))